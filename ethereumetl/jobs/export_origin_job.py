from ethereumetl.executors.batch_work_executor import BatchWorkExecutor
from blockchainetl.jobs.base_job import BaseJob
from ethereumetl.utils import validate_range

from ethereumetl.mappers.receipt_log_mapper import EthReceiptLogMapper
from ethereumetl.mappers.origin_mapper import OriginMarketplaceListingMapper, OriginShopProductMapper
from ethereumetl.service.origin_extractor import OriginEventExtractor


# Addresses of the marketplace contracts.
ORIGIN_MARKETPLACE_V0_CONTRACT_ADDRESS = '0x819Bb9964B6eBF52361F1ae42CF4831B921510f9'
ORIGIN_MARKETPLACE_V1_CONTRACT_ADDRESS = '0x698Ff47B84837d3971118a369c570172EE7e54c2'

# Block number at which contracts were deployed to the Mainnet.
ORIGIN_MARKETPLACE_V0_BLOCK_NUMBER_EPOCH = 6436157
ORIGIN_MARKETPLACE_V1_BLOCK_NUMBER_EPOCH = 8582597


class ExportOriginJob(BaseJob):
    def __init__(
            self,
            start_block,
            end_block,
            batch_size,
            web3,
            ipfs_client,
            marketplace_listing_exporter,
            shop_product_exporter,
            max_workers):
        validate_range(start_block, end_block)
        self.start_block = start_block
        self.end_block = end_block

        self.web3 = web3

        self.marketplace_listing_exporter = marketplace_listing_exporter
        self.shop_product_exporter = shop_product_exporter

        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)

        self.event_extractor = OriginEventExtractor(ipfs_client)

        self.receipt_log_mapper = EthReceiptLogMapper()
        self.marketplace_listing_mapper = OriginMarketplaceListingMapper()
        self.shop_listing_mapper = OriginShopProductMapper()
        self._supports_eth_newFilter = True


    def _start(self):
        pass

    def _export(self):
        pass

    def _export_batch(self, block_number_batch):
        pass

    def _end(self):
        pass
