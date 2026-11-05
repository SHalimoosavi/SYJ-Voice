# Security Policy

Active development. Do not expose this stack to untrusted public traffic or use for production calling.

## Threat model
Assets: credentials, refresh tokens, SIP/TURN secrets, contacts, call metadata, carrier credentials and sponsor funds. Threats: account takeover, credential stuffing, WebSocket impersonation, call spam, toll fraud, SIP scanning, caller-ID spoofing, TURN abuse, denial of service, privilege escalation and data leakage.

## Required controls
- Argon2id password hashing; never store plaintext passwords.
- Short-lived access tokens and revocable/rotated refresh tokens.
- Rate limits for registration, login, refresh, signalling and call initiation.
- Authenticated WebSockets, origin validation and message-size/schema limits.
- Per-user call concurrency and destination allowlists.
- Scoped, expiring SIP/TURN credentials; never commit secrets.
- Restrictive Asterisk dialplans and ACLs; management interfaces private.
- No outbound PSTN by default; reject calls without approved route and funded sponsorship.
- Secrets from deployment secret management, never frontend variables.
- Audit privileged actions; minimise call metadata.
- Dependency/container scanning, backups and incident response.

Independent security review, fraud testing and privacy/legal assessment required before production.
