from bing_images import bing


def downloader(keyword, num_of_images):
    bing.download_images(keyword,
                         num_of_images,
                         output_dir="/home/manav/PycharmProjects/image_filtering_webapp/image_filter"
                                    "/filter_app/downloaded_images",
                         pool_size=10,
                         force_replace=True,
                         extra_query_params='&first=1')
