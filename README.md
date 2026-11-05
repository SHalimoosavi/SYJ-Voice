# SYJ Voice

Open-source, self-hostable global communication platform by SAYANJALI NEXUS PRIVATE LIMITED.

**Status:** Phase 0 foundation in progress. This branch is an early engineering baseline, not a production-ready calling service.

## Product goals
- Free app-to-app internet calling.
- Browser-to-SIP calling through self-hosted Asterisk.
- Optional sponsored PSTN through vendor-neutral SIP trunk adapters.
- Initial destination numbering plans: Germany (+49), United Kingdom (+44), United States (+1), India (+91).

Ordinary telephone-network termination is not inherently free. PSTN must remain disabled unless an authorised carrier route and sufficient sponsor funding are configured. No carrier agreement, telecom authorisation or free termination is implied by this software.

## Technology
- Web: Next.js, TypeScript, SIP.js and WebRTC
- API: Python 3.12, FastAPI, SQLAlchemy 2 and Alembic
- Data: PostgreSQL; Redis planned for transient coordination/rate limiting
- Telephony: Asterisk/PJSIP; coturn TURN template
- Deployment: Docker Compose
- CI: GitHub Actions

## Repository layout
- backend/: API, authentication foundation, persistence models and migrations
- web/: Next.js browser application shell
- telephony/: Asterisk development configuration
- deploy/: Docker Compose and coturn configuration
- docs/: architecture, security and architecture decision records

## Local development
1. Copy .env.example to .env and replace all development secrets with strong random values.
2. Review deploy/docker-compose.yml and the firewall/network notes before exposing any service.
3. Run: docker compose --env-file .env -f deploy/docker-compose.yml up --build
4. API liveness: http://localhost:8000/health/live
5. API readiness: http://localhost:8000/health/ready

This Compose topology is a local development baseline, not a hardened public deployment. Database and Redis have no host ports. SIP, RTP and TURN ports are not published in this baseline; therefore browser telephony cannot work externally until an explicit, reviewed network configuration is added. Asterisk management interfaces must remain private.

## Current implementation status
- Present: initial FastAPI app and health endpoints, SQLAlchemy models, Argon2 password helpers, access-token helper, registration/login route foundation, initial Alembic migration, Next.js landing shell, Asterisk development dialplan/template, coturn template, Dockerfiles, Compose baseline, CI workflows and architecture/security documentation.
- Not yet implemented or verified: refresh-token endpoint/rotation, API rate limiting, authenticated user/profile/contact APIs, WebSocket signalling, browser-to-browser WebRTC, SIP credential provisioning, browser-to-SIP calls, DTMF/hang-up lifecycle, PBX CDR ingestion, full Playwright/integration tests, Nginx/Caddy TLS, OpenTelemetry and production TURN configuration.
- Sponsorship ledger and carrier adapters are Phase 2 and are not implemented.
- No emergency calling, public telephone numbers or guarantee of free calls to ordinary telephone numbers.

Do not use with real users or production credentials until implementation, security, privacy, telecom and operational reviews are complete.

## Licensing
No project-wide license has been selected. See docs/adr/0001-license-not-selected.md. Do not describe the repository as licensed open source until the owner selects and approves a license. Third-party dependencies retain their own licenses.
