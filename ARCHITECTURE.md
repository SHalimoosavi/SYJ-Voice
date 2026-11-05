# Architecture

Web: Next.js, SIP.js, WebRTC, authenticated API and signalling. API: FastAPI identity, profiles, contacts, call metadata and policy. Signalling: authenticated WebSocket relays SDP/ICE; it does not carry audio. Media: WebRTC direct where possible, coturn relay otherwise. PBX: Asterisk/PJSIP handles SIP. Data: PostgreSQL authoritative; Redis transient only. PSTN: future carrier adapter boundary, disabled by default.

## App-to-app flow
Authenticate; open signalling WebSocket; invite callee; exchange SDP offer/answer and ICE; establish DTLS-SRTP media direct or via TURN; persist call lifecycle events.

## Browser-to-SIP flow
Provision scoped SIP credentials; SIP.js registers over secure WebSocket; Asterisk negotiates WebRTC media; restrictive dialplan routes approved destinations; DTMF and hang-up use SIP; PBX events feed CDR storage.

Compose is local development, not HA production. Production requires DNS, TLS, UDP media/TURN reachability, firewall policy, monitoring, backups and hardened PBX/SBC boundaries. Browser clients are untrusted. Asterisk management remains private. Carrier connectivity is disabled until approved.
