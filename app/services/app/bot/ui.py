def deal_card(status):
    progress = {
        "created": "░░░░░ 0%",
        "accepted": "██░░░ 25%",
        "paid": "████░ 75%",
        "completed": "█████ 100%"
    }

    return f"""
🧪 <b>ESCROW DEMO MODE</b>
━━━━━━━━━━━━━━━
⚠️ Payments are NOT REAL

Status: <b>{status.upper()}</b>

Progress:
<code>{progress[status]}</code>

✨ Demo simulation only
"""
