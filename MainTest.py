from anonympy.pdf import pdfAnonymizer
from transformers import pipeline

from transformers import AutoTokenizer, AutoModel
# model='cointegrated/rubert-tiny2',
# tokenizer= 'cointegrated/rubert-tiny2'

anonym = pdfAnonymizer(path_to_pdf = "/home/tawerka/projects/cybergarden/testJPG.jpg",
                       # model='ai-forever/ruBert-base',
                       # tokenizer= 'ai-forever/ruBert-base'
                       )


# Calling the generic function
anonym.anonymize(output_path = './deoutput13rubert-base.pdf',
                     remove_metadata = True,
                     fill = 'black',
                     outline = 'black',
                    )

