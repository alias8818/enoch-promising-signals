# Evidence Ledger for Tiny Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-local-agents-7b0d6d45e8f9`
Run ID: `evidence-ledger-for-tiny-local-agents-7b0d6d45e8f9-20260524T235620269272+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f7b1369e92e7

## What looked useful

At capacity 48, ledger accuracy was 0.5586 versus 0.4008 for tiny_notes, and unsupported answer rate was 0.0000 versus 0.1606. The no-trust-filter ledger matched the baseline, localizing the gain to source-aware evidence discipline.

## Boundaries and scale limits

Synthetic simulator only; no real LLM, embedding retrieval, natural-language extraction, human grading, adversarial source ambiguity, or production agent loop was tested. Main run used 500 scenarios and 10000 answers per agent; capacity sweep used 300 scenarios per capacity.

## Claim scope

In a deterministic synthetic local-document update QA task with trusted facts, trusted updates, untrusted rumors, and equal retained-observation capacity, a source-aware evidence ledger reduced unsupported answers and improved current-fact accuracy versus an unstructured tiny note buffer.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy and supports only the mechanism, not real-agent or publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up using a real tiny local open-weight model with noisy retrieved/tool documents, extracted ledger claims, citation enforcement, and the same accuracy/unsupported-answer metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Model Evidence Ledger QA Probe
- Success threshold: At least 30% relative reduction in unsupported answer rate versus scratchpad baseline with non-overlapping or clearly improved confidence intervals and no more than 5% relative accuracy loss.
- Stop condition: Stop if the ledger cannot be populated reliably from model outputs, if unsupported-answer reduction is below 10% relative in a 500-query pilot, or if the method requires materially more context/state than the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-local-agents-7b0d6d45e8f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
