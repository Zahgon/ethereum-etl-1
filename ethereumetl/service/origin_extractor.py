import base58
import logging

from ethereumetl.utils import hex_to_dec, to_normalized_address
from ethereumetl.ipfs.origin import get_origin_marketplace_data

#
LISTING_CREATED_TOPIC = '0xec3d306143145322b45d2788d826e3b7b9ad062f16e1ec59a5eaba214f96ee3c'
LISTING_UPDATED_TOPIC = '0x470503ad37642fff73a57bac35e69733b6b38281a893f39b50c285aad1f040e0'
PROCESSABLE_TOPICS = [LISTING_CREATED_TOPIC, LISTING_UPDATED_TOPIC]

TOPICS_LEN = 2

logger = logging.getLogger(__name__)


# Helper function. Converts a bytes32 hex string to a base58 encoded ipfs hash.
# For example:
#   "0x017dfd85d4f6cb4dcd715a88101f7b1f06cd1e009b2327a0809d01eb9c91f231"
#   --> "QmNSUYVKDSvPUnRLKmuxk9diJ6yS96r1TrAXzjTiBcCLAL"
def hex_to_ipfs_hash(param):
    pass


# Helper function. Composes an Origin Protocol fully-qualified listing id.
# Its format is "<ethereum_network_id>-<contract_version>-<marketplace_listing_id>"
# For example:
#   "1-001-272" refers to listing 272 on marketplace contract version 1, on Mainnet.
def compose_listing_id(network_id, contract_version, listing_id):
    pass


class OriginEventExtractor(object):
    def __init__(self, ipfs_client):
        self.ipfs_client = ipfs_client

    def extract_event_from_log(self, receipt_log, contract_version):
        pass
