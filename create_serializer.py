from serializers.json_serializer import JsonSerializer
from serializers.yaml_serializer import YamlSerializer


def create_serializer(language):
    if language == "json":
        return JsonSerializer()
    if language == "yaml":
        return YamlSerializer()


def create_serializer_file(language, input_file=""):
    if input_file == "":
        return create_serializer(language)
    else:
        extension = input_file.rpartition(".")[2]
        if extension == language:
            return create_serializer(language)
        else:
            return create_serializer(extension)
