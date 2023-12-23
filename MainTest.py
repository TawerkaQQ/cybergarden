from anonympy.pdf import pdfAnonymizer
from transformers import AutoTokenizer, AutoModel

anonym = pdfAnonymizer(path_to_pdf = "/home/tawerka/projects/cybergarden/open-data-anonimizer/test1JPG.pdf")

# Calling the generic function
anonym.anonymize(output_path = './deoutput5.pdf',
                     remove_metadata = True,
                     fill = 'black',
                     outline = 'black')