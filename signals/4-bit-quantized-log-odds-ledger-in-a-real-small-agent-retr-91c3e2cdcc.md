# 4-bit quantized log-odds ledger in a real small-agent retrieval QA loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-quantized-log-odds-ledger-in-a-real-small-agent-retr-91c3e2cdcc`
Run ID: `4-bit-quantized-log-odds-ledger-in-a-real-small-agent-retr-91c3e2cdcc-20260608T095145310216+0000`

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

- Parent run decision: 4-Bit Evidence Ledger for Small Agents: enoch://control-plane/projects/4-bit-evidence-ledger-for-small-agents-b51f9b145438/runs/4-bit-evidence-ledger-for-small-agents-b51f9b145438-20260608T051911922376+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

Main run: q4 final accuracy 0.8399, fp32 final accuracy 0.8354, stateless final accuracy 0.5557; q4/fp32 answer agreement 0.9659; mean absolute quantization belief error 0.1002 log-odds; theoretical storage reduction 87.5% per cell.

## Boundaries and scale limits

Synthetic corpus only; binary attributes only; deterministic extractor rather than LLM answerer; top-1 unseen retrieval loop; 48,000 QA turns on one seed for the main run; no public benchmark or human-authored corpus.

## Claim scope

In a controlled synthetic small-agent retrieval QA loop with binary attributes, noisy contradictory passages, deterministic lexical retrieval, and deterministic evidence extraction, a signed 4-bit quantized log-odds ledger preserved final-answer accuracy within 2 percentage points of a full-precision ledger while outperforming stateless retrieval.

## Why it stopped

Tier 1 direct controlled test passed the stated mechanism threshold, but the evidence is synthetic and deterministic, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded public-dataset follow-up using a small language-model answerer and the same stateless/fp32/q4 controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 4-bit log-odds ledger with a small LM answerer on public retrieval QA
- Success threshold: q4 final-answer accuracy within 3 percentage points of fp32 ledger and at least 5 percentage points above stateless retrieval across at least three random seeds or fixed dataset splits.
- Stop condition: Stop if q4 falls more than 5 percentage points below fp32 or fails to beat stateless by 3 percentage points on two independent seeds/splits.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-log-odds-ledger-in-a-real-small-agent-retr-91c3e2cdcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
