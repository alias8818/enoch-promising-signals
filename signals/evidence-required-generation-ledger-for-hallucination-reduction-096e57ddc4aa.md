# Evidence-Required Generation Ledger for Hallucination Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-required-generation-ledger-for-hallucination-reduction-096e57ddc4aa`
Run ID: `evidence-required-generation-ledger-for-hallucination-reduction-096e57ddc4aa-20260529T031711170987+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87997efde574

## What looked useful

Evidence-ledger prompting can induce conservative abstention, but small models may fail the ledger format and over-abstain on answerable evidence; naive prompt-only ledgers are not a reliable hallucination-reduction intervention in this bounded test.

## Boundaries and scale limits

One small seq2seq instruction model, synthetic single-passage QA, short contexts, deterministic decoding, no real retrieval corpus, no stronger chat model, no constrained decoding, and no external verifier loop.

## Claim scope

In a synthetic short-context QA harness using google/flan-t5-small, a naive evidence-required ledger prompt improved abstention on unanswerable questions but reduced answerable accuracy enough to slightly worsen overall unsupported answer rate versus a baseline context-grounded prompt.

## Why it stopped

Bounded local evidence is mixed and not paper-ready: the ledger prompt improved unanswerable abstention from 0.0000 to 0.8333 but worsened answerable accuracy from 0.6250 to 0.1667 and overall unsupported rate from 0.5833 to 0.6111.

## Recommended next action

Run a bounded deepen follow-up with constrained ledger validation or a stronger local instruction model, requiring lower unsupported rate without a material answerable-accuracy collapse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained Evidence Ledger Validation for Short-Context QA
- Success threshold: Unsupported rate at least 20% relative lower than baseline, unanswerable abstention accuracy at least 0.80, answerable accuracy no more than 0.05 absolute below baseline, and malformed-ledger rate below 0.05.
- Stop condition: Stop if constrained validation still reduces answerable accuracy by more than 0.10 absolute or fails to reduce unsupported rate relative to baseline on the same 1440-generation harness.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-required-generation-ledger-for-hallucination-reduction-096e57ddc4aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
