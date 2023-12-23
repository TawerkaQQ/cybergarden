import aspose.words as aw

fileNames = []

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

for fileName in fileNames:
    builder.insert_image(fileName)
    # Вставляем разрыв абзаца, чтобы изображения не перекрывались.
    builder.writeln()

doc.save("Output.pdf")
