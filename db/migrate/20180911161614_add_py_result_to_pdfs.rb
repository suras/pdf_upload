class AddPyResultToPdfs < ActiveRecord::Migration[5.2]
  def change
    add_column :pdfs, :py_result, :text
  end
end
