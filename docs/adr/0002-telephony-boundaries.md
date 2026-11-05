# ADR 0002: Separate control plane, media and PSTN

Status: Accepted initial design. Date: 2026-11-05.

FastAPI owns identity, policy and call metadata. WebRTC carries app-to-app media. Asterisk/PJSIP handles SIP. coturn relays media when needed. PSTN adapters remain disabled until an authorised carrier and funding policy are approved.

This reduces trust coupling and prevents an unrestricted toll gateway. SIP provisioning, PBX event ingestion, TURN credential issuance and firewall rules remain implementation tasks.
