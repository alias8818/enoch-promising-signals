# Small Transformer Test of Real Paraphrase Augmentation Under Scarce Pretraining

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `small-transformer-test-of-real-paraphrase-augmentation-und-63181cd4cb`
Run ID: `small-transformer-test-of-real-paraphrase-augmentation-und-63181cd4cb-20260531T163043703348+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Round-Trip Paraphrase Augmentation for Scarce Pretraining: enoch://control-plane/projects/round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864/runs/round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864-20260530T073203458439+0000
- Parent run decision: Neural Scarce-Pretraining Test of Round-Trip Paraphrase Augmentation: enoch://control-plane/projects/neural-scarce-pretraining-test-of-round-trip-paraphrase-au-a71fbb4afc/runs/neural-scarce-pretraining-test-of-round-trip-paraphrase-au-a71fbb4afc-20260531T123557234933+0000

## What looked useful

Real paraphrase augmentation did not meet the Tier 2 threshold: versus the no-augmentation baseline it reduced mean MRPC accuracy by 0.0637 and official F1 by 0.1069 across seeds, with losses on those metrics in all 3 seeds. It produced a small mean balanced-accuracy gain of 0.0104, but this did not beat the duplicate-text control gain of 0.0177 and came with lower macro-F1.

## Boundaries and scale limits

Small custom encoder, word-level vocabulary, GLUE QQP/MRPC only, 600 pretraining source pairs, 120 MLM steps, 256 labeled MRPC examples, three seeds. This is not GPT-2-scale or datacenter-scale evidence and does not establish behavior for larger pretrained LMs or broader paraphrase corpora.

## Claim scope

Three-seed CPU experiment with a custom small Transformer: scarce MLM pretraining on sampled QQP text followed by scarce 256-example balanced MRPC fine-tuning. Real QQP paraphrase augmentation was compared with no-augmentation, duplicate-text, and random non-paraphrase controls under fixed training steps.

## Why it stopped

Medium fixed-seed direct test with real baseline and controls failed the success threshold: real paraphrase augmentation was not consistently better than no augmentation and did not beat the matched-size duplicate control.

## Recommended next action

Stop this follow-up as no-paper evidence; do not escalate real paraphrase augmentation under this scarce-pretraining setup unless a future design first fixes the accuracy/F1 regression and beats duplicate-text controls on paired seeds.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-test-of-real-paraphrase-augmentation-und-63181cd4cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
