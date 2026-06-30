# Evidence-Ledger Agent Reliability Test on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-test-on-cpu-e1ac8f5a49b6`
Run ID: `evidence-ledger-agent-reliability-test-on-cpu-e1ac8f5a49b6-20260611T011413762662+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a9b0134a6fab

## What looked useful

Evidence ledgers can help as a reliability mechanism when source metadata is reliable and abstention is allowed, but treating verified primary evidence as authoritative creates a sharp failure mode under corrupt-primary conditions.

## Boundaries and scale limits

Synthetic generated tasks only; no LLM reasoning, real retrieval, natural-language evidence extraction, production agent loop, or external corpus was tested. The main run used 5,000 CPU-generated tasks and completed in 31.21 seconds.

## Claim scope

In a deterministic synthetic fact-retrieval harness, an evidence-ledger answer selector using source class, verification, recency, and abstention improved accuracy and reduced hallucination versus overlap, majority, and no-abstain controls when trusted metadata was reliable, but failed on corrupt trusted-primary evidence.

## Why it stopped

No-paper useful signal: mechanism-level synthetic evidence supports a scoped benefit and exposes a failure boundary, but it is proxy evidence rather than direct production-agent validation.

## Recommended next action

Run a bounded deepen follow-up with a small real LLM/retrieval-agent harness over text snippets, requiring preserved noisy/stale benefits plus corrupt-primary detection through contradiction checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-snippet Evidence Ledger With Corrupt-Primary Contradiction Checks
- Success threshold: Ledger agent improves overall accuracy by at least 10 percentage points versus non-ledger control, reduces hallucination by at least 20 percentage points versus no-abstain control, and detects or abstains on at least 50% of corrupt-primary cases without losing more than 5 percentage points on clean cases.
- Stop condition: Stop as negative if corrupt-primary detection is below 25%, if hallucination is not reduced versus no-abstain control, or if ledger traces cannot be audited reliably.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-test-on-cpu-e1ac8f5a49b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
