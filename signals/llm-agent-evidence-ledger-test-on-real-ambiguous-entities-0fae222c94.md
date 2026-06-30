# LLM-agent evidence ledger test on real ambiguous entities

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-agent-evidence-ledger-test-on-real-ambiguous-entities-0fae222c94`
Run ID: `llm-agent-evidence-ledger-test-on-real-ambiguous-entities-0fae222c94-20260608T012212636381+0000`

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

- Parent run decision: Tiny CPU Agent Evidence Ledger: enoch://control-plane/projects/tiny-cpu-agent-evidence-ledger-94882e94540e/runs/tiny-cpu-agent-evidence-ledger-94882e94540e-20260607T161009722547+0000
- Parent run decision: Evidence ledger on semi-real ambiguous-entity agent QA: enoch://control-plane/projects/evidence-ledger-on-semi-real-ambiguous-entity-agent-qa-abcedd59af/runs/evidence-ledger-on-semi-real-ambiguous-entity-agent-qa-abcedd59af-20260607T201212681089+0000

## What looked useful

Explicit evidence ledgers with source-weighted evidence can prevent distractor context from dominating ambiguous entity resolution; equal-weight evidence ablation nearly erased the gain.

## Boundaries and scale limits

Queries were generated from static checked entity evidence after live Wikipedia API access was rate-limited, and the resolver is a deterministic ledger scorer rather than a full LLM-agent with live retrieval or tool-use traces.

## Claim scope

On 141 fixed-seed generated ambiguous-entity examples over 48 real candidate entities, a deterministic source-weighted evidence ledger resolved all examples and beat a flat TF-IDF candidate-evidence baseline by 51.8 accuracy points; the effect was mainly due to clause/source weighting rather than category evidence.

## Why it stopped

No-paper useful signal: medium fixed-seed evidence supports the mechanism, but the static/generated query design and non-LLM scorer are not publication-grade direct evidence.

## Recommended next action

Run a deepen follow-up on held-out human-authored ambiguous-entity queries with a real prompted LLM baseline and the same evidence-ledger bookkeeping.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger LLM agent on held-out human ambiguous-entity queries
- Success threshold: Ledger-prompted LLM improves exact entity accuracy by at least 10 percentage points over the non-ledger LLM baseline and by at least 5 points over a retrieval-only baseline, with the source-weight ablation losing at least half of the gain.
- Stop condition: Stop as unsupported if ledger accuracy gain is below 5 points versus the non-ledger LLM baseline or if the source-weight ablation preserves nearly all of the gain.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-evidence-ledger-test-on-real-ambiguous-entities-0fae222c94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
