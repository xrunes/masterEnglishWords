import random
import os
a = [
    'impact',
    'regret',
    'hostile',
    'fascinate',
    'squeeze',
    'freeze',
    'approval',
    'parcel',
    'count',
    'expel',
    'external',
    'missile',
    'punish',
    'frighten',
    'standard',
    'category',
    'cruel',
    'nerve',
    'brain',
    'peasant',
    'remedy',
    'cough',
    'dialect',
    'earn',
    'intimidate',
    'impress',
    'expert',
    'bait',
    'deserve',
    'popularity',
    'oven',
    'bear',
    'yoghurt',
    'flavor',
    'charcoal',
    'heat',
    'express',
    'terrify',
    'crow',
    'conclusion',
    'plot',
    'fund',
    'anxiety',
    'junior',
    'effort',
    'attempt',
    'shade',
    'summary',
    'nail',
    'realize',
    'polite',
    'form',
    'upset',
    'graphic',
    'lent',
    'plastic',
    'religious',
    'gender',
    'wise',
    'single',
    'live',
    'silly',
    'corn',
    'rule',
    'fluent',
    'prevent',
    'discover',
    'naughty',
    'obtain',
    'disappoint',
    'attract',
    'attractive'
    'pub',
    'effect',
    'cast',
    'depend',
    'prince',
    'marry',
    'stuff',
    'staff',
    'span',
    'convince',
    'slave',
    'opening',
    'ethnic',
    'kindness',
    'confirm',
    'couch',
    'damage',
    'tent',
    'describe',
    'layer',
    'graceful',
    'grace',
    'elegant',
    'clap',
    'tax',
    'compare',
    'so-called',
    'blend',
    'cure',
    'situation',
    'social',
    'passenger',
    'invent',
    'analysis',
    'throat',
    'invest',
    'positive',
    'consume',
    'gather',
    'chase',
    'specify',
    'creature',
    'cloak',
    'solar',
    'race',
    'attention',
    'mind',
    'kidney',
    'organic',
    'cash',
    'entertain',
    'pollute',
    'fuel',
    'prepare',
    'dealer',
    'horrible',
    'fold',
    'remain',
    'pace',
    'silence',
    'statue',
    'gain',
    'ankle',
    'identical',
    'praise',
    'motivate',
    'opinion',
    'record',
    'habit',
    'custom',
    'university',
    'career',
    'ensure',
    'extent',
    'district'
    'protect',
    'numerous',
    'lift',
    'shift',
    'flat',
    'costume',
    'grape',
    'escape',
    'protein',
    'embarrass',
    'consist',
    'curtain',
    'premise',
    'horror',
    'cave',
    'bucket',
    'drag',
    'maintain',
    'solid',
    'narrow',
    'mess',
    'lack',
    'symbol',
    'dove',
    'response',
    'invite',
    'fansy',
    'restaurant',
    'detect',
    'minor',
    'approve',
    'emperor',
    'predict',
    'cotton',
    'kettle',
    'imply',
    'region',
    'harden',
    'course',
    'logic',
    'disable',
    'lawyer',
    'lean',
    'physical',
    'board',
    'arrow',
    'rotate',
    'desire',
    'labor',
    'concern',
    'owner',
    'secure',
    'quest',
    'expend',
    'suit',
    'amaze',
    'forgive',
    'flow',
    'rage',
    'imagine',
    'medical',
    'claw',
    'crab',
    'satisfy',
    'term',
    'core',
    'awake',
    'factory',
    'focus',
    'measure',
    'discuss',
    'terror',
    'detail',
    'pattern',
    'quality',
    'stress',
    'reduce',
    'expense',
    'publish',
    'decorate',
    'loose',
    'theater',
    'prove',
    'drama',
    'whale',
    'risk',
    'shape',
    'compete',
    'private',
    'starve',
    'silent',
    'original',
    'analyze',
    'occupy',
    'obvious',
    'precise',
    'spare',
    'decent',
    'quantity',
    'demand',
    'acquire',
    'sudden',
    'fairy',
    'palm',
    'suffer',
    'journal',
    'frequent',
    'sort',
    'bull',
    'journey',
    'efficient',
    'limited',
    'mystery',
    'comment',
    'youth',
    'shave',
    'relieve',
    'thirst',
    'muscle',
    'elbow',
    'lens',
    'bald',
    'recipe',
    'psychology',
    'suspicious',
    'acquaint',
    'strike',
    'hay',
    'communication',
    'beneath',
    'permission',
    'consensus',
    'reel',
    'legacy',
    'powder',
    'torch',
    'envisages',
    'proceedings',
    'precedent',
    'inquiry',
    'limb',
    'identification',

    'Christian',
    'cemetery',
    'incorporates',
    'reconcile',
    'blush',
    'bore',
    'facility',
    'merit',
    'oppress',
    'contempt',
    'wealth',
    'impetus',
    'spacecraft',
    'assume',
    'magistrate',
    'idiom',
    'negative',
    'jurisdiction',
    'compensate',
    'diabetes',
    'dedicate',
    'incentive',
    'combine',
    'assistance',
    'automatic',
    'coronavirus',
    'horn',
    'humanity',
    'epoch',
    'blunt',
    'brake',
    'role',
    'assumption',
    'differ',
    'napkin',
    'patent',
    'emergency',
    'economic',
    'hook',
    'delicate',
    'claim',
    'perpetual',
    'overlook',
    'dialogue',
    'medal',
    'frim',
    'advocate',
    'elect',
    'blossom',
    'lamp',
    'negligible',
    'initiate',
    'perhaps',
    'value',
    'germ',
    'beware',
    'sow',
    'establish',
    'affiliate',
    'modify',
    'rip',
    'recruit',
    'deliberate',
    'forbit',
    'hail',
    'degree',
    'extensive',
    'expire',
    'fever',
    'curious',
    'nylon',
    'assembly',
    'generalize',
    'accuse',
    'gaze',
    'abstract',
    'dome',
    'credential',
    'stare',
    'explicit',
    'machine',
    'intrigue',
    'anchor',
    'defy',
    'harness',
    'ignorance',
    'amend',
    'spontaneous',
    'sponge',
    'advertise',
    'inquire',
    'realm',
    'corporate',
    'coal',
    'heir',
    'prior',
    'engagement',
    'gasoline',
    'swing',
    'deem',
    'choke',
    'goodness',
    'tempo',
    'reach',
    'gradual', # The graph shows a gradual increase.
    'hut',
    'further',
    'administration',
    'facet',
    'diamond',
    'instinct',
    'distill',
    'tan',
    'outing',
    'alcohol',
    'irritate',
    'futile',
    'chemistry',
    'commission',
    'disorder',
    'ore',
    'forehead',
    'peculiar',
    'immense',
    'confine',
    'cop',
    'foul',
    'chew',
    'instantaneous',
    'guarantee',
    'tension',
    'deteriorate',
    'garage',
    'employer',
    'isle',
    'reform',
    'cautious',
    'consider',
    'refund',
    'rational',
    'funeral',
    'fundamental',
    'pronunciation',
    'occupation',
    'abdomen',
    'faith',
    'bill',
    'resolution',
    'remnant',
    'equipment',
    'ambassador',
    'comprehend',
    'harsh',
    'pepper',
    'dilemma',
    'innumerable',
    
    'preface',
    'endow',
    'severe',
    'emloy',
    'hen',
    'aftermath',
    'inward',
    'discard',
    'string',
    'nasty',
    'explosion',
    'expertise',
    'plate',
    'sacred',
    'destructive',
    'stoop',
    'commonwealth',
    'plaster',
    'denial',
    'laundry',
    'outskirts',
    'geology',
    'scholar',
    'eve',
    'spur',
    'stability',
    'tangible',
    'deceit',
    'supply',
    'bud',
    'reap',
    'stage',
    'judicial',
    'neutron',
    'illegal',
    'discrepancy',
    'coil',
    'treat',
    'obligation',
    'punch',
    'ebb',
    'pessimistic',
    'holy',
    'pulse',
    'detach',
    'strip',
    'detain',
    'internal',
    'strategy',
    'ashamed',
    'smuggle',
    'rank',
    'reproduce',
    'oval',
    'democratic',
    'indignation',
    'gown',
    'herald',
    'advisable',
    'scope',
    'county',
    'distinguish',
    'decline',
    'scrape',
    'toilet',
    'backward',
    'adopt',
    'court',
    'remark',
    'durable',
    'sight',
    'militant',
    'embody',
    'straightforward',
    'moral',
    'convention',
    'cozy',
    'superstition',
    'fur',
    'salute',
    'kit',
    'mammals',
    'bundle',
    'specialize',
    'knock',
    'litter',
    'accurate',
    'monarch',
    'hinge',
    'escalate',
    'brandy',
    'hormone',
    'inflation',
    'reliance',
    'horsepower',
    'premium',
    'probability',
    'definition',
    'characteristic',
    'nonetheless',
    'contest',
    'huddle',
    'generous',
    'offend',
    'due',
    'afterward',
    'breakdown',
    'mug',
    'champagne',
    'porter',
    'denote',
    'likewise',
    'congratulation',
    'incline',
    'identify',
    'astonish',
    'cabin',
    'odor',
    'recreation',
    'chairman',
    'spelling',
    'highway',
    'dwell',
    'executive',
    'recollect',
    'seize',
    'slender',
    'poet',
    'realistic',
    'formulate',
    'pump',
    'opt',
    'former',
    'provide',
    'convict',
    'segment',
    'membership',
    'imminent',
    'ounce',
    'concert',
    'adapt',
    'crown',
    'object',
    'conversion',
    'plural',
    'courtyard',
    'jungle',
    'confront',
    'stable',
    'stain',
    'goose',
    'legitimate',
    'snack',
    'patriotic',
    'mentor',
    'painting',
    'alter',
    'comic',
    'favor',
    'coward',
    'competition',
    'plateau',
    'nephew',
    'projector',
    'mold',
    'apology',
    'comfort',
    'massive',
    'repay',
    'energetic',
    'technical',
    'pad',
    'slight',
    'psychiatry',
    'evidence',
    'commute',
    'applause',
    'outdoor',
    'emphasis',
    'essence',
    'consistent',
    'policy',
    'commodity',
    'industry',
    'observation',
    'athlete',
    'parameter',
    'magnitude',
    'rebellion',
    'steel',
    'intermediate',
    'considerable',
    'subscribe',
    'matter',
    'bite',
    'nod',
    'liability',
    'withhold',
    'international',
    'intelligible',
    'eliminate',
    'erupt',
    'admire',
    'spokeperson',
    'envy',
    'path',
    'ashore',
    'benign',
    'calcium',
    'surrender',
    'liberal',
    'contain',
    'president',
    'misunderstand',
    'prototype',
    'recovery',
    'linger',
    'postage',
    'distinction',
    'reassure',
    'additional',
    'scale',
    'locality',
    'eternal',
    'endorse',
    'namely',
    'convenience',
    'hesitate',
    'deputy',
    'sneeze',
    'desirable',
    'zebra',
    'figure',
    'pharmacy',
    'punctual',
    'acid',
    'survive',
    'drum',
    'spot',
    'current',
    'badge',
    'conspiracy',
    'cooperative',
    'density',
    'dirt',
    'decisive',
    'mass',
    'sew',
    'idle',
    'impair',
    'mosaic',
    'thigh',
    'circumstance',
    'eyesight',
    'partly',
    'compose',
    'insulate',
    'cruise',
    'nap',
    'appetite',
    'marginal',
    'distinct',
    'fine',
    'alert',
    'fence',
    'divide',
    'exist',
    'elevate',
    'ban',
    'assert',
    'solitary',
    'strengthen',
    'mood',
    'square',
    'controversy',
    'expectation',
    'exploit',
    'slum',
    'lateral',
    'household',
    'royalty',
    'freelance',
    'safeguard',
    'southern',
    'patron',
    'inference',
    'extra',
    'conversation',
    'implement',
    'stance',
    'linguistic',
    'architect',
    'outcome',
    'apartment',
    'saint',
    'silk',
    'lonely',
    'pretent',
    'exceed',
    'compel',
    'constitute',
    'piece',
    'allege',
    'jar',
    'organize',
    'ape',
    'extreme',
    'clash',
    'remainder',
    'comprehensive',
    'band',
    'passion',
    'indulge',
    'advanced',
    'pollution',
    'security',
    'exert',
    'pilgrim',
    'pity',
    'nearly',
    'repetition',
    'sentiment',
    'gasp',
    'mount',
    'grasp',
    'practice',
    'leading',
    'echo',
    'eclipse',
    'scarcely',
    'poetry',
    'obstruction',
    'scrutiny',
    'solemn',
    'hijack',
    'clinic',
    'pocket',
    'centigrade',
    'heroin',
    'waterfall',
    'sweater',
    'sideways',
    'tempt',
    'bibliography',
    'compliment',
    'living',
    'rather',
    'submarine',
    'critic',
    'mute',
    'owing to',
    'appendix',
    'puff',
    'messenger',
    'catalog',
    'exact',
    'innovation',
    'palace',
    'continent',
    'pickup',
    'register',
    'opportunity',
    'charge',
    'respect',
    'sarcastic',
    'weight',
    'literary',
    'construct',
    'maneuver',
    'exception',
    'arbitrary',
    'dozen',
    'cheat',
    'automobile',
    'lure',
    'position',
    'swarm',
    'integrate',
    'kick',
    'hatred',
    'stool',
    'avail',
    'liter',
    'ambition',
    'host',
    'apart',
    'opposite',
    'direct',
    'extend',
    'compartment',
    'seem',
    'arena',
    'expedition',
    'gesture',
    'stern',
    'candle',
    'incidence',
    'plea',
    'participate',
    'approach',
    'spicy',
    'stroke',
    'streamline',
    'pond',
    'ruthless',
    'academic',
    'configuration',
    'sharp',
    'nationality',
    'longitude',
    'abide',
    'withdraw',
    'establish',
    'silver',
    'absorb',
    'champion',
    'hint',
    'priority',
    'legislation',
    'plight',
    'accessory',
    'restraint',
    'broadcast',
    'divident',
    'microphone',
    'auditorium',
    'weigh',
    'lord',
    'modernization',
    'dubious',
    'deviated',
    'diverse',
    'ample',
    'illustrate',
    'preside',
    'circus',
    'rape',
    'raise',
    'nurture',
    'nostalgic',
    'mental',
    'pint',
    'cellar',
    'sail',
    'military',
    'amplify', # COVID-19 has amplified the demand for masks.
    'debut',
    'provoke',
    'opponet',
    'cocaine',
    'meter',
    'soak', # Soak the soybeans overnight, and they'll be soft by morning.
    'hollow',
    'superficial',
    'intuition',
    'belly',
    'dose',
    'complex',
    'emotion',
    'sociable',
    'consequence',
    'recur',
    'inhabitant',
    ]

while True:
    b = random.sample(a, 1)
    print(b)
    os.system('pause')