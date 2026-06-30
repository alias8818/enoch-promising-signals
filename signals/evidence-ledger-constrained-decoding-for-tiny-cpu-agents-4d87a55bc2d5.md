# Evidence-ledger constrained decoding for tiny CPU agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-constrained-decoding-for-tiny-cpu-agents-4d87a55bc2d5`
Run ID: `evidence-ledger-constrained-decoding-for-tiny-cpu-agents-4d87a55bc2d5-20260607T153415353634+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de5906dc8f62

## What looked useful

Ledger constraints were effective for citation validity/support in the proxy. Strict answer-from-ledger decoding helped answer accuracy only when the evidence selector was adequate; with weak evidence signal it preserved support but reduced answer accuracy. Post-hoc retry was slower and much less effective at support.

## Boundaries and scale limits

No real LLM, natural-language corpus, retrieval system, or production agent runtime was tested. Results are mechanism evidence only; answer accuracy remained evidence-selection limited and degraded as ledger size increased.

## Claim scope

Synthetic noisy-scorer evidence-ledger probe: constrained evidence-ID decoding eliminated invalid citations, and answer-from-ledger decoding eliminated unsupported answer/citation pairs across generated ledgers of size 4, 16, and 64.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy only, not direct validation on a real tiny CPU agent.

## Recommended next action

Run a bounded direct-model follow-up with a small quantized CPU model on factual QA ledgers, comparing free JSON, retry validation, constrained IDs, and answer-from-evidence decoding on answer accuracy, support, invalid citations, and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-CPU-model validation of evidence-ledger constrained decoding
- Success threshold: At ledger sizes of at least 16, constrained decoding should improve support rate by at least 50 percentage points over free JSON while losing no more than 5 percentage points of answer accuracy and adding no more than 25% end-to-end latency versus unconstrained decoding.
- Stop condition: Stop if constrained decoding cannot be integrated with a local CPU model, or if support improves by less than 20 percentage points or answer accuracy drops by more than 10 percentage points on the first 200 evaluated examples.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constrained-decoding-for-tiny-cpu-agents-4d87a55bc2d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
