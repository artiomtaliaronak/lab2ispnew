import logging
from create_serializer import create_serializer_file as serializer

logging.basicConfig(
    level=logging.WARNING, filename="warning.log"
)


def string_converter(string, input_language, output_language):
    if input_language == output_language:
        return string
    loader = serializer(input_language)
    dumper = serializer(output_language)
    return dumper.dumps(loader.loads(string))


def file_converter(input_path, output_path, in_lang="json", out_lang="json"):
    try:
        loader = serializer(in_lang, input_path)
        dumper = serializer(out_lang, output_path)
        if loader is dumper:
            logging.info("Don't need to convert")
            return
        with open(input_path, "r") as fp:
            loaded_data = loader.load(fp)

        with open(output_path, "w") as fp:
            dumper.dump(loaded_data, fp)

    except TypeError as e:
        logging.warning(f"Warning: {e}")
