import logging
import re

from ethereumetl.domain.origin import OriginMarketplaceListing, OriginShopProduct
from ethereumetl.ipfs.client import IpfsClient

logger = logging.getLogger('origin')

IPFS_PRIMARY_GATEWAY_URL = 'https://cf-ipfs.com/ipfs'
IPFS_SECONDARY_GATEWAY_URL = 'https://gateway.ipfs.io/ipfs'

# Returns an IPFS client that can be used to fetch Origin Protocol's data.
def get_origin_ipfs_client():
    pass


# Parses the shop's HTML index page to extract the name of the IPFS directory under
# which all the shop data is located.
def _get_shop_data_dir(shop_index_page):
    pass


# Returns the list of products from an Origin Protocol shop.
def _get_origin_shop_products(receipt_log, listing_id, ipfs_client, shop_ipfs_hash):
    pass

# Returns a listing from the Origin Protocol marketplace.
def get_origin_marketplace_data(receipt_log, listing_id, ipfs_client, ipfs_hash):
    # Load the listing's metadata from IPFS.
    pass


