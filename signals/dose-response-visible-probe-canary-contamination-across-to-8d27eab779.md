# Dose-response visible-probe canary contamination across tokenization and small pretrained models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dose-response-visible-probe-canary-contamination-across-to-8d27eab779`
Run ID: `dose-response-visible-probe-canary-contamination-across-to-8d27eab779-20260610T071531798372+0000`

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

- Parent run decision: Direct small-model canary trust scoring under visible-probe contamination: enoch://control-plane/projects/direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4/runs/direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4-20260610T025059535603+0000
- Parent run decision: Held-out Canary Probe Trust Scoring: enoch://control-plane/projects/held-out-canary-probe-trust-scoring-8eb74a912e19/runs/held-out-canary-probe-trust-scoring-8eb74a912e19-20260609T174310610179+0000

## What looked useful

Both distilgpt2 and gpt2 showed a reproducible dose-response: dose 0 never recovered the canary; dose 1 was weak or seed-sensitive; dose 8 made every model/variant rank the true canary above decoys; dose 64 saturated. Common-word 4-token canaries had much larger margins and exact greedy recovery at dose 8, while 16-token rare alphanumeric canaries had smaller margins and only 50% exact recovery at dose 8.

## Boundaries and scale limits

Not a paper-positive or internet-scale contamination audit: synthetic templated data only, GPT-2-family models/tokenizers only, two seeds, short fixed-step fine-tuning, no persistence-after-clean-training test, no instruction-tuned or larger models.

## Claim scope

Synthetic visible-probe canary fine-tuning on distilgpt2 and gpt2 with two fixed seeds, two GPT-2-family tokenization variants, doses 0/1/8/64, and matched decoy likelihood plus greedy extraction metrics.

## Why it stopped

Tier 2 medium confirmation produced a useful scoped mechanism signal, but evidence is too synthetic and narrow for publication readiness.

## Recommended next action

Run a bounded deepen study with intermediate doses 2/4/6/8/12, more seeds, a non-GPT tokenizer/model family, and a clean-finetuning persistence check before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Threshold and persistence of visible-probe canary extraction across tokenizers
- Success threshold: Common-word canaries reach at least 75% exact greedy recovery at a lower dose than fragmented alphanumeric canaries in at least two model/tokenizer families, with positive best-decoy margin and rank 1 in at least 90% of successful-threshold conditions.
- Stop condition: Stop as negative or mixed if intermediate-dose curves do not separate by tokenization in two model families or if exact recovery disappears after clean-finetuning persistence checks.

## Evidence references

- Artifact root: `<local-path>/projects/dose-response-visible-probe-canary-contamination-across-to-8d27eab779`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
