# Natural-text transformer check for n-gram gradient fingerprint consensus

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-text-transformer-check-for-n-gram-gradient-fingerp-87f7c334af`
Run ID: `natural-text-transformer-check-for-n-gram-gradient-fingerp-87f7c334af-20260526T165231280285+0000`

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

- Parent run decision: N-Gram Gradient Fingerprint Consensus: enoch://control-plane/projects/n-gram-gradient-fingerprint-consensus-5e4abd11eb59/runs/n-gram-gradient-fingerprint-consensus-5e4abd11eb59-20260525T214501069897+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e860e91d93dc

## What looked useful

Pretrained distilgpt2 passed the predeclared Tier 1 consensus threshold: same-phrase mean cosine 0.1952 versus cross-phrase 0.0248, delta 0.1704, permutation p=0.0004998 over 36 occurrences. A random-initialized distilgpt2 control also passed and was stronger: delta 0.5068, p=0.0004998, so the signal is real for this gradient representation but not evidence of a learned natural-text-specific mechanism.

## Boundaries and scale limits

Hand-curated sentences only; distilgpt2 only; input-embedding gradients only; no naturally sampled corpus n-grams, GPT-2-small-class baseline, larger models, full parameter gradients, or token-identity-subtracted controls.

## Claim scope

In a controlled 36-occurrence natural-English phrase test on distilgpt2, localized input-embedding gradients for repeated 3-token n-grams showed higher same-phrase cosine alignment than cross-phrase controls.

## Why it stopped

No-paper closure: the direct Tier 1 threshold was met, but the random-initialized control showed a larger consensus effect, so the learned natural-text transformer interpretation is unsupported by this run.

## Recommended next action

Run a bounded deepen test on naturally sampled corpus n-grams using layer-wise activation or parameter-gradient fingerprints with matched random-init, token-shuffled, and token-identity-subtracted controls; stop treating the current input-gradient result as a learned natural-text mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-identity-controlled corpus n-gram gradient fingerprint consensus
- Success threshold: On at least 100 naturally sampled n-gram occurrences across at least 20 n-gram types, the pretrained model's token-identity-subtracted consensus delta must be >= 0.05 above random-init and shuffled controls with p <= 0.05.
- Stop condition: Stop if pretrained residual consensus is not above both random-init and token-shuffled controls by 0.05, or if the effect appears only in input embeddings and disappears in deeper layer or parameter-gradient fingerprints.

## Evidence references

- Artifact root: `<local-path>/projects/natural-text-transformer-check-for-n-gram-gradient-fingerp-87f7c334af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
