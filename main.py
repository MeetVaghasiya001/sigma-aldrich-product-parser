import os
import gzip
import json
from request_data import price_request
from urllib.parse import urljoin
from model import *
from db import *
from concurrent.futures import ThreadPoolExecutor,as_completed
from lxml import html

create_db()
pending_file()
main_folder_path= 'C:/Users/meet.vaghasiya/Desktop/bif files/sigmal_rich_json' 

all_files = os.listdir(main_folder_path)

def clean_html(text):
    try:
        return html.fromstring(text).text_content() if text else ""
    except Exception:
        return text or ""

def gzip_unzip(file_name):
    try:
        path = os.path.join(main_folder_path, file_name)
        with gzip.open(path, 'rt', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def process(file_name):
    data = json.loads(gzip_unzip(file_name))

    main_url = 'https://www.sigmaaldrich.com/'

    props = data.get('props') or {}
    page = props.get('pageProps') or {}
    core = ((page.get('data') or {}).get('getProductDetail')) or {}

    substance = core.get('substance') or {}
    brand = core.get('brand') or {}

    product_name = clean_html(substance.get('name'))
    product_brand = brand.get('erpKey')
    material_id = core.get('materialIds')
    product_number = core.get('productNumber')
    product_key = core.get('productKey')

    price = []
    try:
        json_data = {
            'operationName': 'PricingAndAvailability',
            'variables': {
                'displaySDS': False,
                'productNumber': product_number,
                'materialIds': material_id,
                'brand': product_brand,
                'quantity': 1,
                'catalogType': 'sial',
                'orgId': None,
                'checkForPb': True,
                'dealerId': '',
                'checkBuyNow': True,
                'productKey': product_key,
                'cachedPriceOnly': False,
            },
            'query': 'query PricingAndAvailability($productNumber: String!, $brand: String, $quantity: Int!, $catalogType: CatalogType, $checkForPb: Boolean, $orgId: String, $materialIds: [String!], $displaySDS: Boolean = false, $dealerId: String, $checkBuyNow: Boolean, $productKey: String, $erp_type: [String!], $cachedPriceOnly: Boolean) {\n  getPricingForProduct(\n    input: {productNumber: $productNumber, brand: $brand, quantity: $quantity, catalogType: $catalogType, checkForPb: $checkForPb, orgId: $orgId, materialIds: $materialIds, dealerId: $dealerId, checkBuyNow: $checkBuyNow, productKey: $productKey, erp_type: $erp_type, cachedPriceOnly: $cachedPriceOnly}\n  ) {\n    ...ProductPricingDetail\n    __typename\n  }\n}\n\nfragment ProductPricingDetail on ProductPricing {\n  dealerId\n  productNumber\n  country\n  materialPricing {\n    ...ValidMaterialPricingDetail\n    __typename\n  }\n  discontinuedPricingInfo {\n    ...DiscontinuedMaterialPricingDetail\n    __typename\n  }\n  dchainMessage\n  productInfo {\n    ...ProductInfoMessageDetail\n    __typename\n  }\n  __typename\n}\n\nfragment ValidMaterialPricingDetail on ValidMaterialPricing {\n  brand\n  type\n  currency\n  dealerId\n  listPriceCurrency\n  listPrice\n  shipsToday\n  freeFreight\n  catalogType\n  marketplaceOfferId\n  marketplaceSellerId\n  materialDescription\n  materialNumber\n  materialId\n  netPrice\n  packageSize\n  packageType\n  price\n  isBuyNow\n  product\n  productGroupSBU\n  productHierarchy\n  ecomStrikeThroughPrice\n  quantity\n  isPBAvailable\n  vendorSKU\n  isBlockedProduct\n  hidePriceMessageKey\n  expirationDate\n  leadTime\n  availableQtyInStock\n  availabilities {\n    ...Availabilities\n    __typename\n  }\n  additionalInfo {\n    ...AdditionalInfo\n    __typename\n  }\n  promotionalMessage {\n    ...PromotionalMessage\n    __typename\n  }\n  ... @include(if: $displaySDS) {\n    sdsLanguages\n    __typename\n  }\n  minOrderQuantity\n  __typename\n}\n\nfragment Availabilities on MaterialAvailability {\n  date\n  key\n  plantLoc\n  quantity\n  displayFromLink\n  displayInquireLink\n  messageType\n  contactInfo {\n    contactPhone\n    contactEmail\n    __typename\n  }\n  availabilityOverwriteMessage {\n    messageKey\n    messageValue\n    messageVariable1\n    messageVariable2\n    messageVariable3\n    __typename\n  }\n  supplementaryMessage {\n    messageKey\n    messageValue\n    messageVariable1\n    messageVariable2\n    messageVariable3\n    __typename\n  }\n  __typename\n}\n\nfragment AdditionalInfo on CartAdditionalInfo {\n  carrierRestriction\n  unNumber\n  tariff\n  casNumber\n  jfcCode\n  pdcCode\n  __typename\n}\n\nfragment PromotionalMessage on PromotionalMessage {\n  messageKey\n  messageValue\n  messageVariable1\n  messageVariable2\n  messageVariable3\n  __typename\n}\n\nfragment DiscontinuedMaterialPricingDetail on DiscontinuedMaterialPricing {\n  errorMsg\n  paramList\n  hideReplacementProductLink\n  displaySimilarProductLabel\n  hideTechnicalServiceLink\n  replacementProducts {\n    ...ReplacementProductDetail\n    __typename\n  }\n  alternateMaterials {\n    ...AlternateMaterialDetail\n    __typename\n  }\n  __typename\n}\n\nfragment ReplacementProductDetail on Product {\n  productNumber\n  name\n  description\n  sdsLanguages\n  images {\n    mediumUrl\n    altText\n    __typename\n  }\n  brand {\n    key\n    erpKey\n    name\n    logo {\n      smallUrl\n      altText\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment AlternateMaterialDetail on Material {\n  number\n  __typename\n}\n\nfragment ProductInfoMessageDetail on ProductInfoMessage {\n  productNumber\n  messageType\n  message\n  __typename\n}',
        }
        price_data = price_request(json_data)  
        if price_data:
            price_data = json.loads(price_data)
            pricing = ((price_data.get('data') or {}).get('getPricingForProduct') or {})
            price_path = pricing.get('materialPricing') or []

            for p in price_path:
                price.append({
                    'size': p.get('packageSize'),
                    'price': p.get('netPrice'),
                    'package_type': p.get('packageType'),
                    'sku': p.get('materialNumber')
                })
    except:
        pass

    alies = [
        {'key': a.get('label'), 'value': a.get('value')}
        for a in (core.get('aliases') or [])
    ]

    description = clean_html(core.get('description'))

    descriptions = [
        {'key': d.get('label'), 'value': clean_html(",".join(d.get('values') or []))}
        for d in (core.get('descriptions') or [])
    ]

    images = [
        urljoin(main_url, i.get('largeUrl'))
        for i in (core.get('images') or [])
        if i.get('largeUrl')
    ]

    attributes = [
        {'key': a.get('label'), 'value': ",".join(a.get('values') or [])}
        for a in (core.get('attributes') or [])
    ]

    safty_info = [
        {'key': s.get('key'), 'value': s.get('value')}
        for s in (core.get('compliance') or [])
    ]

    data = {
        'product_name': product_name,
        'description': description,
        'product_brand': product_brand,
        'material_id': material_id,
        'product_number': product_number,
        'product_key': product_key,
        'price': price,
        'alies': alies,
        'descriptions': descriptions,
        'images': images,
        'attributes': attributes,
        'safty_info': safty_info
    }

    print(f"{product_key} was added.")

    try:
        validate = ProductResponse(**data)
        if validate:
            return validate.model_dump()
    except:
        data = {
                'file_name':file_name,
                'status':'pending'
            }
        insert_pending_data(data)
        return None
row = []
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(process, f) for f in all_files]

    for future in as_completed(futures):
        r = future.result()
        if not r:
            print('recode skiped')
            continue

        row.append((
            r.get('product_name'),
            r.get('description'),
            r.get('product_brand'),
            r.get('product_number'),
            r.get('product_key'),
            json.dumps(r.get('material_id')),
            json.dumps(r.get('price')),
            json.dumps(r.get('alies')),
            json.dumps(r.get('descriptions')),
            json.dumps(r.get('images')),
            json.dumps(r.get('attributes')),
            json.dumps(r.get('safty_info')),
            'success'
        ))

        if len(row) == 10:
            insert_data(row)
            row.clear()

if row:
    insert_data(row)
