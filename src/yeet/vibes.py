"""
Maximum shitpost energy messages
"""
import random

ANALYZING = [
    "analyzing slop...",
    "detecting vibes...",
    "running the algorithms...",
    "consulting the oracle...",
    "asking ChatGPT (jk it's Claude)...",
    "sniffing your codebase...",
    "judging your tech stack...",
]

DEPLOYING = [
    "yeeting to the cloud...",
    "slapping that slop online...",
    "sending it...",
    "shipping this bad boy...",
    "deploying the vibes...",
    "making it live fr fr...",
]

SUCCESS = [
    "we're so back",
    "it's up",
    "slop deployed successfully",
    "your app is live bestie",
    "congrats you shipped something",
    "ok it's actually done",
]

FIRE_RESPONSES = [
    "your slop is fire 🔥 no cap",
    "app is bussin fr fr 🔥",
    "this finna be fire 🔥",
    "sheeeesh it's actually working 🔥",
    "ngl your app kinda goes hard 🔥",
    "respectfully, this slaps 🔥",
]

MID_RESPONSES = [
    "app responding but kinda mid ngl",
    "it's up but it's giving nothing",
    "works but at what cost (2.5s response time)",
    "technically functional i guess",
    "alive but barely",
    "running but make it slower",
]

COOKED_RESPONSES = [
    "bruh your app is cooked 💀",
    "it's so over 💀",
    "app machine broke 💀",
    "404 brain not found 💀",
    "down catastrophic 💀",
    "bro it's literally dead 💀",
    "press F to pay respects 💀",
]

ERROR_RESPONSES = [
    "something went wrong bestie",
    "error occurred fr",
    "this ain't it chief",
    "broke af rn",
    "yeah this failed",
    "L + ratio + deployment failed",
]


def random_analyzing() -> str:
    return random.choice(ANALYZING)


def random_deploying() -> str:
    return random.choice(DEPLOYING)


def random_success() -> str:
    return random.choice(SUCCESS)


def random_fire() -> str:
    return random.choice(FIRE_RESPONSES)


def random_mid() -> str:
    return random.choice(MID_RESPONSES)


def random_cooked() -> str:
    return random.choice(COOKED_RESPONSES)


def random_error() -> str:
    return random.choice(ERROR_RESPONSES)
