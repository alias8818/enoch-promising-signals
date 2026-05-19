# Internal KV-cache anchors versus prompt-token anchors on episodic recall

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `internal-kv-cache-anchors-versus-prompt-token-anchors-on-e-55a2892ad1`
Run ID: `internal-kv-cache-anchors-versus-prompt-token-anchors-on-e-55a2892ad1-20260519T110357972601+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Internal KV-cache anchors versus prompt-token anchors on episodic recall: internal_generated:internal-kv-cache-anchors-versus-prompt-token-anchors-on-e-55a2892ad1

## What looked useful

Across two pretrained causal LMs, prompt-token episode context and the same episode prefilled into past_key_values produced identical accuracies and near-zero paired margin deltas, with max full-vocab logit deltas below 0.0004. Query-only, wrong-episode, and anchor-only controls showed no KV-specific recall benefit.

## Boundaries and scale limits

Validated on distilgpt2 and GPT-2 small with 1000 deterministic synthetic examples per model. This does not test learned latent KV slots, trained cache-retrieval architectures, 7B+ long-context models, or multi-hour corpus-scale episodic recall.

## Claim scope

For prompt-derived episode anchors in standard causal LMs, prefilled KV-cache anchors are numerically equivalent to the same visible prompt-token anchors and do not provide a distinct episodic-recall advantage on the tested synthetic forced-choice recall task.

## Why it stopped

Direct bounded validation on two models falsified the stated prompt-derived KV-cache anchor advantage: the cache path was numerically equivalent to the prompt-token path, so there is no distinct mechanism to scale in this form.

## Recommended next action

Stop this prompt-derived KV-anchor line as no-paper evidence; only pursue a new bounded test if the mechanism is changed to learned latent KV slots or a non-equivalent cache-retrieval module with a parameter-matched prompt-token baseline.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Learned latent KV slots versus parameter-matched prompt-token memory
- Success threshold: At least +5 percentage points forced-choice accuracy or at least +0.10 mean log-prob margin over the parameter-matched prompt-token baseline on held-out episodes, with no corresponding gain on wrong-memory controls and stable results across at least three seeds.
- Stop condition: Stop if the learned latent KV variant is within +/-2 percentage points accuracy and +/-0.03 mean margin of the prompt-token baseline, or if gains also appear on wrong-memory controls.

## Evidence references

- Artifact root: `<local-path>/projects/internal-kv-cache-anchors-versus-prompt-token-anchors-on-e-55a2892ad1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
