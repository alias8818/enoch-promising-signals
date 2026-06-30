# Human-Labeled Semantic False Accept Test for Tiered Evidence Ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `human-labeled-semantic-false-accept-test-for-tiered-eviden-922945005b`
Run ID: `human-labeled-semantic-false-accept-test-for-tiered-eviden-922945005b-20260612T061913146128+0000`

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

- Parent run decision: Falsifiable Evidence Ledger with Tiered Validation: enoch://control-plane/projects/falsifiable-evidence-ledger-with-tiered-validation-421bc729f683/runs/falsifiable-evidence-ledger-with-tiered-validation-421bc729f683-20260612T052130669313+0000
- Parent run decision: Real-Corpus False Accept and False Reject Test for Tiered Evidence Ledgers: enoch://control-plane/projects/real-corpus-false-accept-and-false-reject-test-for-tiered-6d1bf1278b/runs/real-corpus-false-accept-and-false-reject-test-for-tiered-6d1bf1278b-20260612T061403981974+0000

## What looked useful

Tiered gates reduced false accept rate versus flat similarity on MRPC from 0.930 to 0.558, on PAWS from 0.777 to 0.761, and on RTE from 0.855 to 0.534. The effect came with recall losses of 0.154 on MRPC, 0.013 on PAWS, and 0.226 on RTE; F1 did not improve over flat similarity. Against logistic TF-IDF, the ledger had lower false accepts only on MRPC.

## Boundaries and scale limits

Sentence-pair proxy only; no full retrieval pipeline, document provenance ledger, multi-hop evidence, LLM verifier, production abstention calibration, or fresh human audit labels. Validation used public human-labeled datasets and CPU-local lexical/TF-IDF methods.

## Claim scope

On PAWS, MRPC, and RTE human-labeled sentence-pair validation splits, a deterministic tiered lexical evidence ledger reduced semantic false accept rate versus a flat TF-IDF similarity acceptor, but did not improve F1 and did not dominate a learned TF-IDF logistic baseline.

## Why it stopped

Tier 2 direct metrics support the false-accept-reduction mechanism versus a flat baseline, but not a paper-ready superiority claim because utility tradeoffs are substantial and a real learned TF-IDF baseline is competitive or better on two of three datasets.

## Recommended next action

Stop this run as no-paper useful signal; a future bounded deepen test should use a real retrieval corpus plus NLI verifier calibration if the controller wants to test whether ledger gates add value beyond learned semantic baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retrieval-backed NLI calibration test for tiered evidence ledgers
- Success threshold: At least 20% relative false accept rate reduction versus the learned semantic baseline on the held-out set with recall drop no greater than 5 percentage points and non-overlapping bootstrap interval favoring the ledger.
- Stop condition: Stop if the ledger cannot beat the learned semantic baseline under the recall-loss constraint on the held-out set, or if gains appear only against flat lexical similarity.

## Evidence references

- Artifact root: `<local-path>/projects/human-labeled-semantic-false-accept-test-for-tiered-eviden-922945005b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
