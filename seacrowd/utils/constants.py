from enum import Enum
from types import SimpleNamespace
from collections import defaultdict
from seacrowd.utils.schemas import (
    kb_features,
    qa_features,
    text2text_features,
    text_features,
    text_multi_features,
    pairs_features,
    pairs_multi_features,
    pairs_features_score,
    seq_label_features,
    ssp_features,
    speech_text_features,
    speech2speech_features,
    image_text_features,
)

METADATA: dict = {
    "_LOCAL": bool,
    "_LANGUAGES": str,
    "_DISPLAYNAME": str,
}

SEACrowdValues = SimpleNamespace(NULL="<SEACROWD_NULL_STR>")

# Default View Name
DEFAULT_SOURCE_VIEW_NAME = "source"
DEFAULT_SEACROWD_VIEW_NAME = "seacrowd"


class Tasks(Enum):
    DEPENDENCY_PARSING = "DEP"
    WORD_SENSE_DISAMBIGUATION = "WSD"
    WORD_ANALOGY = "WA"
    KEYWORD_EXTRACTION = "KE"
    COREFERENCE_RESOLUTION = "COREF"

    # Single Text Classification
    SENTIMENT_ANALYSIS = "SA"
    ASPECT_BASED_SENTIMENT_ANALYSIS = "ABSA"
    EMOTION_CLASSIFICATION = "EC"
    HOAX_NEWS_CLASSIFICATION = "HNC"
    INTENT_CLASSIFICATION = "INT"
    TAX_COURT_VERDICT = "TACOS"
    LEGAL_CLASSIFICATION = "LC"
    RHETORIC_MODE_CLASSIFICATION = "RMC"
    TOPIC_MODELING = "TL"

    # Single Text Sequence Labeling
    POS_TAGGING = "POS"
    KEYWORD_TAGGING = "KT"
    NAMED_ENTITY_RECOGNITION = "NER"
    SENTENCE_ORDERING = "SO"
    SLOT_FILLING = "SF"

    # Pair Text Classification
    QUESTION_ANSWERING = "QA"
    TEXTUAL_ENTAILMENT = "TE"
    SEMANTIC_SIMILARITY = "STS"
    NEXT_SENTENCE_PREDICTION = "NSP"
    SHORT_ANSWER_GRADING = "SAG"
    MORPHOLOGICAL_INFLECTION = "MOR"
    CONCEPT_ALIGNMENT_CLASSIFICATION = "CAC"

    # Single Text Generation
    MACHINE_TRANSLATION = "MT"
    PARAPHRASING = "PARA"
    SUMMARIZATION = "SUM"
    MULTILEXNORM = "MLN"

    # Multi Text Generation
    DIALOGUE_SYSTEM = "DS"

    # Self Supervised Pretraining
    SELF_SUPERVISED_PRETRAINING = "SSP"

    # SpeechText
    SPEECH_RECOGNITION = "ASR"
    SPEECH_TO_TEXT_TRANSLATION = "STTT"
    TEXT_TO_SPEECH = "TTS"

    # SpeechSpeech
    SPEECH_TO_SPEECH_TRANSLATION = "S2ST"

    # ImageText
    IMAGE_CAPTIONING = "IC"
    STYLIZED_IMAGE_CAPTIONING = "SIC"
    VISUALLY_GROUNDED_REASONING = "VGR"

    # No seacrowd schema
    FACT_CHECKING = "FCT"
    
class Licenses(Enum):
    # BSD
    BSD = "BSD license family (bsd)"
    BSD_2_CLAUSE = "BSD 2-clause “Simplified” license (bsd-2-clause)"
    BSD_3_CLAUSE = "BSD 3-clause “New” or “Revised” license (bsd-3-clause)"
    BSD_3_CLAUSE_CLEAR = "BSD 3-clause Clear license (bsd-3-clause-clear)"
    
    # Creative Common
    CC = "Creative Commons license family (cc)"
    CC0_1_0 = "Creative Commons Zero v1.0 Universal (cc0-1.0)"
    CC_BY_2_0 = "Creative Commons Attribution 2.0 (cc-by-2.0)"
    CC_BY_2_5 = "Creative Commons Attribution 2.5 (cc-by-2.5)"
    CC_BY_3_0 = "Creative Commons Attribution 3.0 (cc-by-3.0)"
    CC_BY_4_0 = "Creative Commons Attribution 4.0 (cc-by-4.0)"
    CC_BY_SA_3_0 = "Creative Commons Attribution Share Alike 3.0 (cc-by-sa-3.0)"
    CC_BY_SA_4_0 = "Creative Commons Attribution Share Alike 4.0 (cc-by-sa-4.0)"
    CC_BY_NC_2_0 = "Creative Commons Attribution Non Commercial 2.0 (cc-by-nc-2.0)"
    CC_BY_NC_3_0 = "Creative Commons Attribution Non Commercial 3.0 (cc-by-nc-3.0)"
    CC_BY_NC_4_0 = "Creative Commons Attribution Non Commercial 4.0 (cc-by-nc-4.0)"
    CC_BY_ND_4_0 = "Creative Commons Attribution No Derivatives 4.0 (cc-by-nd-4.0)"
    CC_BY_NC_ND_3_0 = "Creative Commons Attribution Non Commercial No Derivatives 3.0 (cc-by-nc-nd-3.0)"
    CC_BY_NC_ND_4_0 = "Creative Commons Attribution Non Commercial No Derivatives 4.0 (cc-by-nc-nd-4.0)"
    CC_BY_NC_SA_2_0 = "Creative Commons Attribution Non Commercial Share Alike 2.0 (cc-by-nc-sa-2.0)"
    CC_BY_NC_SA_3_0 = "Creative Commons Attribution Non Commercial Share Alike 3.0 (cc-by-nc-sa-3.0)"
    CC_BY_NC_SA_4_0 = "Creative Commons Attribution Non Commercial Share Alike 4.0 (cc-by-nc-sa-4.0)"
    CDLA_SHARING_1_0 = "Community Data License Agreement – Sharing, Version 1.0 (cdla-sharing-1.0)"
    CDLA_PERMISSIVE_1_0 = "Community Data License Agreement – Permissive, Version 1.0 (cdla-permissive-1.0)"
    CDLA_PERMISSIVE_2_0 = "Community Data License Agreement – Permissive, Version 2.0 (cdla-permissive-2.0)"
    WTFPL = "Do What The F*ck You Want To Public License (wtfpl)"
    ECL_2_0 = "Educational Community License v2.0 (ecl-2.0)"
    
    # EPL
    EPL_1_0 = "Eclipse Public License 1.0 (epl-1.0)"
    EPL_2_0 = "Eclipse Public License 2.0 (epl-2.0)"
    EUPL_1_1 = "European Union Public License 1.1 (eupl-1.1)"
    
    # GPL
    AGPL_3_0 = "GNU Affero General Public License v3.0 (agpl-3.0)"
    GFDL = "GNU Free Documentation License family (gfdl)"
    GPL = "GNU General Public License family (gpl)"
    GPL_2_0 = "GNU General Public License v2.0 (gpl-2.0)"
    GPL_3_0 = "GNU General Public License v3.0 (gpl-3.0)"
    LGPL = "GNU Lesser General Public License family (lgpl)"
    LGPL_2_1 = "GNU Lesser General Public License v2.1 (lgpl-2.1)"
    LGPL_3_0 = "GNU Lesser General Public License v3.0 (lgpl-3.0)"
    LGPL_LR = "Lesser General Public License For Linguistic Resources (lgpl-lr)"

    # OTHER SPECIFIC LICENSES
    APACHE_2_0 = "Apache license 2.0 (apache-2.0)"
    MIT = "MIT (mit)"
    C_UDA = "Computational Use of Data Agreement (c-uda)"
    OPENRAIL = "OpenRAIL license family (openrail)"
    BIGSCIENCE_OPENRAIL_M = "BigScience OpenRAIL-M (bigscience-openrail-m)"
    CREATIVEML_OPENRAIL_M = "CreativeML OpenRAIL-M (creativeml-openrail-m)"
    BIGSCIENCE_BLOOM_RAIL_1_0 = "BigScience BLOOM RAIL 1.0 (bigscience-bloom-rail-1.0)"
    BIGCODE_OPENRAIL_M = "BigCode Open RAIL-M v1 (bigcode-openrail-m)"
    AFL_3_0 = "Academic Free License v3.0 (afl-3.0)"
    ARTISTIC_2_0 = "Artistic license 2.0 (artistic-2.0)"
    BSL_1_0 = "Boost Software License 1.0 (bsl-1.0)"
    ISC = "ISC (isc)"
    LPPL_1_3C = "LaTeX Project Public License v1.3c (lppl-1.3c)"
    MS_PL = "Microsoft Public License (ms-pl)"
    MPL_2_0 = "Mozilla Public License 2.0 (mpl-2.0)"
    ODC_BY = "Open Data Commons License Attribution family (odc-by)"
    ODBL = "Open Database License family (odbl)"
    OPENRAIL_PP = "Open Rail++-M License (openrail++)"
    OSL_3_0 = "Open Software License 3.0 (osl-3.0)"
    POSTGRESQL = "PostgreSQL License (postgresql)"
    OFL_1_1 = "SIL Open Font License 1.1 (ofl-1.1)"
    NCSA = "University of Illinois/NCSA Open Source License (ncsa)"
    ZLIB = "zLib License (zlib)"
    PDDL = "Open Data Commons Public Domain Dedication and License (pddl)"
    DEEPFLOYD_IF_LICENSE = "DeepFloyd IF Research License Agreement (deepfloyd-if-license)"
    LLAMA2 = "Llama 2 Community License Agreement (llama2)"
    
    # OTHER UNLISTED / UNLICENSED
    UNLICENSE = "The Unlicense (unlicense)"
    UNKNOWN = "Unknown (unknown)"


TASK_TO_SCHEMA = {
    Tasks.DEPENDENCY_PARSING: "KB",
    Tasks.WORD_SENSE_DISAMBIGUATION: "T2T",
    Tasks.WORD_ANALOGY: "T2T",
    Tasks.KEYWORD_EXTRACTION: "SEQ_LABEL",
    Tasks.COREFERENCE_RESOLUTION: "KB",
    Tasks.DIALOGUE_SYSTEM: "T2T",
    Tasks.NAMED_ENTITY_RECOGNITION: "SEQ_LABEL",
    Tasks.POS_TAGGING: "SEQ_LABEL",
    Tasks.KEYWORD_TAGGING: "SEQ_LABEL",
    Tasks.SENTENCE_ORDERING: "SEQ_LABEL",
    Tasks.SLOT_FILLING: "SEQ_LABEL",
    Tasks.QUESTION_ANSWERING: "QA",
    Tasks.TEXTUAL_ENTAILMENT: "PAIRS",
    Tasks.SEMANTIC_SIMILARITY: "PAIRS_SCORE",
    Tasks.NEXT_SENTENCE_PREDICTION: "PAIRS",
    Tasks.SHORT_ANSWER_GRADING: "PAIRS_SCORE",
    Tasks.MORPHOLOGICAL_INFLECTION: "PAIRS_MULTI",
    Tasks.PARAPHRASING: "T2T",
    Tasks.MACHINE_TRANSLATION: "T2T",
    Tasks.SUMMARIZATION: "T2T",
    Tasks.MULTILEXNORM: "T2T",
    Tasks.SENTIMENT_ANALYSIS: "TEXT",
    Tasks.ASPECT_BASED_SENTIMENT_ANALYSIS: "TEXT_MULTI",
    Tasks.TAX_COURT_VERDICT: "TEXT",
    Tasks.EMOTION_CLASSIFICATION: "TEXT",
    Tasks.LEGAL_CLASSIFICATION: "TEXT",
    Tasks.INTENT_CLASSIFICATION: "TEXT",
    Tasks.RHETORIC_MODE_CLASSIFICATION: "TEXT",
    Tasks.TOPIC_MODELING: "TEXT",
    Tasks.SELF_SUPERVISED_PRETRAINING: "SSP",
    Tasks.SPEECH_RECOGNITION: "SPTEXT",
    Tasks.SPEECH_TO_TEXT_TRANSLATION: "SPTEXT",
    Tasks.TEXT_TO_SPEECH: "SPTEXT",
    Tasks.SPEECH_TO_SPEECH_TRANSLATION: "S2S",
    Tasks.IMAGE_CAPTIONING: "IMTEXT",
    Tasks.STYLIZED_IMAGE_CAPTIONING: "IMTEXT",
    Tasks.VISUALLY_GROUNDED_REASONING: "IMTEXT",
    Tasks.HOAX_NEWS_CLASSIFICATION: "TEXT",
    Tasks.CONCEPT_ALIGNMENT_CLASSIFICATION: "PAIRS",
    Tasks.FACT_CHECKING: None,
}

SCHEMA_TO_TASKS = defaultdict(set)
for task, schema in TASK_TO_SCHEMA.items():
    SCHEMA_TO_TASKS[schema].add(task)
SCHEMA_TO_TASKS = dict(SCHEMA_TO_TASKS)

VALID_TASKS = set(TASK_TO_SCHEMA.keys())
VALID_SCHEMAS = set(TASK_TO_SCHEMA.values())

SCHEMA_TO_FEATURES = {
    "KB": kb_features,
    "QA": qa_features,
    "T2T": text2text_features,
    "TEXT": text_features(),
    "TEXT_MULTI": text_multi_features(),
    "PAIRS": pairs_features(),
    "PAIRS_MULTI": pairs_multi_features(),
    "PAIRS_SCORE": pairs_features_score(),
    "SEQ_LABEL": seq_label_features(),
    "SSP": ssp_features,
    "SPTEXT": speech_text_features,
    "S2S": speech2speech_features,
    "IMTEXT": image_text_features(),
}

TASK_TO_FEATURES = {
    Tasks.NAMED_ENTITY_RECOGNITION: {"entities"},
    Tasks.DEPENDENCY_PARSING: {"relations", "entities"},
    Tasks.COREFERENCE_RESOLUTION: {"entities", "coreferences"},
    # Tasks.NAMED_ENTITY_DISAMBIGUATION: {"entities", "normalized"},
    # Tasks.EVENT_EXTRACTION: {"events"}
}