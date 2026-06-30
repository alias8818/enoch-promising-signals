# Real-trace exact-anchor replay for small CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41`
Run ID: `real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41-20260528T161321080441+0000`

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

- Parent run decision: Exact-anchor evidence ledger for small CPU agents: enoch://control-plane/projects/exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87/runs/exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87-20260528T020551071549+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71f9eafbd9e9

## What looked useful

Exact-anchor replay passed the Tier-1 threshold on real small-agent traces: 4/4 active unsupported baseline finals rejected, 0/3 supported active finals falsely rejected, 100% prefix-shift anchor verification, and 100% cited-evidence tamper detection. Id-only and document-only controls survived all three supported cited tamper cases.

## Boundaries and scale limits

Tiny inherited trace replay only: 16 rows total, 8 baseline rows, deterministic support labels, no new live model generation, simple scalar tool outputs, and no semantic/paraphrase/multi-span audit.

## Claim scope

On 16 inherited real small-agent Qwen CPU tool-use trace rows, exact span+hash evidence anchors can replay final-answer support decisions, reject unsupported active baseline finals, survive harmless prefix offset shifts, and detect controlled cited-evidence tampering.

## Why it stopped

Tier-1 direct replay threshold was met, but the evidence is too small and inherited for paper readiness.

## Recommended next action

Run a prospective live small-agent benchmark with exact anchors enforced during generation on at least 50 held-out tool-use tasks per model, with independent support audit and adversarial stale/tampered evidence cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prospective live exact-anchor generation for small CPU agents
- Success threshold: At least 50% unsupported-final reduction versus citation-only gating, no more than 5 percentage-point exact-match loss, abstention below 20%, and 100% detection of injected cited-evidence tampering on the evaluated set.
- Stop condition: Stop if exact-anchor generation fails to reduce unsupported finals relative to citation-only gating on two tested small-model families, or if abstention exceeds 20% at matched tool-call budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
