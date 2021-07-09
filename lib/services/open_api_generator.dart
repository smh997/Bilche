import 'package:openapi_generator_annotations/openapi_generator_annotations.dart';

@Openapi(
    additionalProperties: AdditionalProperties(
        pubName: 'bilche_api',
        pubAuthor: 'SMH_LS10',
        pubAuthorEmail: 'smh10.mh@gmail.com'),
    inputSpecFile: 'openapi-spec.yaml',
    generatorName: Generator.dart,
    outputDirectory: 'lib/api/bilche')
class Example extends OpenapiGeneratorConfig {}

// flutter pub run build_runner build --delete-conflicting-outputs