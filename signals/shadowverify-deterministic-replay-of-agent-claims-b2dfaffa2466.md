# ShadowVerify: Deterministic Replay of Agent Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `shadowverify-deterministic-replay-of-agent-claims-b2dfaffa2466`
Run ID: `shadowverify-deterministic-replay-of-agent-claims-b2dfaffa2466-20260609T230621875401+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c3df127b157

## What looked useful

ShadowVerify replay reached 100% safe classification on the targeted harness with 0 false accepts and 0 false rejects, while current-state and transcript-only baselines false-accepted post-hoc file tampering or tampered stdout transcripts. Replay overhead was about 91 ms median and 132.6 ms p95 per episode, with 23 MB max RSS over the 400-episode run.

## Boundaries and scale limits

Evidence is limited to 400 synthetic CPU-only local command episodes with simple structured predicates. It does not validate natural-language claim extraction, real LLM agent traces, networked tools, GUI/browser tools, adversarial sandbox escape attempts, or long multi-step repository workflows.

## Claim scope

In a bounded synthetic local-shell harness with structured file and stdout claims, deterministic replay from an initial workspace snapshot accepted deterministic true claims, rejected replay-contradicted false claims, and marked nondeterministic command observations indeterminate.

## Why it stopped

No-paper useful signal: the replay mechanism is supported in a targeted synthetic harness, but direct evidence on real agent claims is missing.

## Recommended next action

Run a bounded deepen follow-up on real saved agent traces with initial filesystem snapshots and structured claim extraction; do not write a paper from this synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: ShadowVerify on Real Agent Trace Claims
- Success threshold: Replay false accept rate at least 50% lower than both baselines, truthful claim false reject rate under 10%, indeterminate rate under 25%, and median replay overhead under 2 seconds per episode on local traces.
- Stop condition: Stop if fewer than 50 real episodes can be replayed from preserved snapshots, if structured claim extraction is not auditable, or if replay accepts any known false claim without flagging a missing dependency or nondeterminism.

## Evidence references

- Artifact root: `<local-path>/projects/shadowverify-deterministic-replay-of-agent-claims-b2dfaffa2466`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
