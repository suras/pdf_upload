class Pdf < ApplicationRecord
	mount_uploader :doc, DocUploader
end
