# Compressed KV agent ledger with exact anchor hashes for tool use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-kv-agent-ledger-with-exact-anchor-hashes-for-tool-use-675d33111061`
Run ID: `compressed-kv-agent-ledger-with-exact-anchor-hashes-for-tool-use-675d33111061-20260525T154931380727+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a571a18fae2a

## What looked useful

Anchor hashes are useful integrity handles for compacted agent ledgers, but they do not by themselves preserve exact old tool-use bytes. KV-only compression was small and queryable but had only 1.8% exact replay availability; adding a content-addressed blob store restored 100% exact replay with only about 3.2% storage reduction on the benchmark.

## Boundaries and scale limits

Synthetic JSON tool traces only; perfect extraction assumed; no real LLM summarization, real agent task success, external blob retrieval, adversarial collision analysis, or production context-window latency measured.

## Claim scope

On deterministic synthetic structured tool traces, a compressed KV ledger with sha256 tool anchors preserved fact lookup and tamper detection while reducing serialized state to about 21.5% of full history, but exact replay of old compacted tool payloads required retaining or retrieving the original payload bytes.

## Why it stopped

Synthetic proxy result: supports a useful mechanism distinction but does not validate real-agent performance or publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up on real agent/tool traces with imperfect extraction and an external content-addressed blob store; stop this run because the current evidence is synthetic mechanism evidence, not paper-grade validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace compressed agent ledger with external exact-payload retrieval
- Success threshold: At least 50% active context byte reduction vs full history, 100% exact replay for cited tool outputs through blob retrieval, 100% tamper rejection, and at least 95% tool-grounded query correctness on real traces.
- Stop condition: Stop if exact replay is below 100%, tamper rejection is below 100%, query correctness drops below 95%, or total storage plus retrieval overhead exceeds full-history retention without a context-window benefit.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-kv-agent-ledger-with-exact-anchor-hashes-for-tool-use-675d33111061`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
