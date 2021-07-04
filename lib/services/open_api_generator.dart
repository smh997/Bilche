import 'package:openapi_generator_annotations/openapi_generator_annotations.dart';

@Openapi(
    additionalProperties:
        AdditionalProperties(pubName: 'bilche_api', pubAuthor: 'SMH'),
    inputSpecFile: 'openapi-spec.yaml',
    generatorName: Generator.dart,
    outputDirectory: 'api/bilche')
class Example extends OpenapiGeneratorConfig {}
