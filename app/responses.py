
from app.database import DBScore, DBMessage

def score_dict(score: DBScore) -> dict:
    return {
        "server": score.server,
        "checksum": score.checksum,
        "submitted_at": score.submitted_at,
        "mode": score.mode,
        "mods": score.mods,
        "user": {
            "id": score.user_id,
            "name": score.user_name,
            "country": score.user_country
        },
        "beatmap": {
            "id": score.beatmap_id,
            "text": score.beatmap_text,
            "checksum": score.beatmap_checksum
        },
        "stats": {
            "pp": score.pp,
            "pp_fc": score.pp_fc,
            "acc": score.acc,
            "total_score": score.total_score,
            "max_combo": score.max_combo,
            "perfect": score.perfect,
            "passed": score.passed,
            "grade": score.grade,
            "c300": score.c300,
            "c100": score.c100,
            "c50": score.c50,
            "cgeki": score.cgeki,
            "ckatu": score.ckatu,
            "cmiss": score.cmiss
        },
        "replay": {
            "filename": score.replay_filename,
            "available": score.replay_available
        }
    }

def message_dict(message: DBMessage) -> dict:
    return {
        "server": message.server,
        "sender_id": message.sender_id,
        "sender_name": message.sender_name,
        "target_name": message.target_name,
        "message": message.message,
        "created_at": message.created_at
    }
