# Self-paraphrase augmentation for tiny local pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-paraphrase-augmentation-for-tiny-local-pretraining-fd624b87c534`
Run ID: `self-paraphrase-augmentation-for-tiny-local-pretraining-fd624b87c534-20260620T132314662626+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9d69bb66242a

## What looked useful

Self-paraphrase augmentation appears to trade original-distribution fit for paraphrase robustness. Gains were very large on paraphrase templates represented during augmentation, small but positive on novel paraphrase templates, and consistently negative on original templates.

## Boundaries and scale limits

CPU-only n-gram proxy; synthetic templated facts; deterministic paraphrases; no neural transformer training, natural corpus, downstream task, or large-scale validation.

## Claim scope

In a five-seed synthetic, equal-token-budget word-level trigram LM proxy, deterministic self-paraphrase augmentation improved held-out paraphrase perplexity but worsened original-template perplexity.

## Why it stopped

Proxy evidence is mixed and not paper-ready: paraphrase validation improved, but original-template validation regressed across every seed.

## Recommended next action

Run one bounded neural-LM deepen test with equal token budgets and require paraphrase gains without material original-distribution regression before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM self-paraphrase augmentation with original-distribution guardrail
- Success threshold: At least 10% mean held-out paraphrase perplexity improvement with no more than 2% mean original-validation perplexity regression, and wins on both criteria in at least 2/3 seeds.
- Stop condition: Stop if original-validation regression exceeds 5% in two seeds or held-out paraphrase improvement is below 5% after the planned bounded neural run.

## Evidence references

- Artifact root: `<local-path>/projects/self-paraphrase-augmentation-for-tiny-local-pretraining-fd624b87c534`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
