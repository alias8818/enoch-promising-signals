# Evidence Ledger SFT for Small Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-sft-for-small-tool-calling-agents-f4fd6b95ee44`
Run ID: `evidence-ledger-sft-for-small-tool-calling-agents-f4fd6b95ee44-20260528T182413236058+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/afdbd41a7a28

## What looked useful

Evidence ledger rows can act as useful selection/grounding scaffolding for a small model when paired with noisy tool transcripts, but this local evidence is not enough for a paper claim.

## Boundaries and scale limits

Single seed, synthetic data, classifier proxy rather than autoregressive SFT, no pretrained LM, no realistic tool benchmark, and all arms failed to learn the tie/same class.

## Claim scope

On a synthetic noisy lookup-transcript task with a 69k-70k parameter GRU classifier, adding a correct claim-specific evidence ledger to the transcript improved held-out final-answer accuracy from 41.6% to 57.3%; corrupting the test ledger reduced accuracy to 41.1%.

## Why it stopped

Closed as no-paper useful signal: the evidence is synthetic/proxy-only and mixed due to complete failure on the same/tie class, despite a positive ledger-vs-plain accuracy delta and corrupted-ledger mechanism check.

## Recommended next action

Run a bounded deepen follow-up with a pretrained GPT-2-small-class causal LM that generates full tool traces plus ledgers, using balanced labels and multi-seed evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive evidence-ledger SFT on balanced synthetic tool traces
- Success threshold: Evidence-ledger SFT beats plain trace SFT by at least 5 absolute accuracy points on final answers, improves or preserves all per-class accuracies including same, and shows a measurable drop under corrupted-ledger evaluation.
- Stop condition: Stop if ledger SFT does not beat plain trace SFT in at least two of three seeds, if same-class accuracy remains near zero, or if corrupted-ledger evaluation does not reduce performance.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-sft-for-small-tool-calling-agents-f4fd6b95ee44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
