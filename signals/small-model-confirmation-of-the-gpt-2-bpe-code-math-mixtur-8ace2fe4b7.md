# Small-model confirmation of the GPT-2 BPE code/math mixture optimum

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `small-model-confirmation-of-the-gpt-2-bpe-code-math-mixtur-8ace2fe4b7`
Run ID: `small-model-confirmation-of-the-gpt-2-bpe-code-math-mixtur-8ace2fe4b7-20260522T122432835811+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tiny-transformer validation of code/math mixture ratios: enoch://control-plane/projects/tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09/runs/tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09-20260522T103404450149+0000
- Parent run decision: Real-tokenizer bounded confirmation of code/math mixture-ratio optimum: enoch://control-plane/projects/real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae/runs/real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae-20260522T111505361609+0000

## What looked useful

Direct held-out losses with GPT-2 BPE and single-domain controls support an interior mixture: endpoints had mean losses 7.9263 (0% code) and 5.4034 (100% code), 50% code had 2.4772, while 25% and 37.5% code averaged 2.3517 and 2.3344 across the targeted two-seed check.

## Boundaries and scale limits

CPU-only local validation; synthetic/deterministic math corpus; local Python-code corpus; 64-token context; 500 train steps per condition; mostly one seed except the two best ratios, which were checked with a second seed. Not GPT-2-scale or public-corpus evidence.

## Claim scope

A 7.23M-parameter GPT-style decoder trained from scratch with GPT-2 BPE on local Python-code tokens and deterministic math text for 500 steps per condition shows an interior code/math mixture optimum on balanced held-out code/math loss, with the best observed band at 25% to 37.5% code and best two-seed average at 37.5% code.

## Why it stopped

Closed as no-paper useful signal: the local small-model evidence supports the mechanism but is not publication-grade due to synthetic/local corpora and small training scale.

## Recommended next action

Run a bounded public-corpus deepen test using real code and math datasets, three fixed seeds, and ratios 0.25/0.375/0.5 with the same GPT-2 BPE tokenizer before considering any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-corpus three-seed check of the 25-37.5% GPT-2 BPE code/math mixture band
- Success threshold: The 0.25-0.375 ratio band beats 0.5 and endpoint controls on mean held-out code/math loss in at least two of three seeds with an average margin of at least 0.05 nats versus 0.5.
- Stop condition: Stop if 0.5 or an endpoint matches/beats the 0.25-0.375 band in two seeds, or if public-corpus preprocessing cannot produce comparable token budgets and held-out splits.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-confirmation-of-the-gpt-2-bpe-code-math-mixtur-8ace2fe4b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
