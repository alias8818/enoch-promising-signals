# Suffix-array speculative draft for local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-draft-for-local-inference-5537e1aa0e0b`
Run ID: `suffix-array-speculative-draft-for-local-inference-5537e1aa0e0b-20260528T100543370175+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a77778913927

## What looked useful

Suffix-array drafting is cheap and high-coverage, but exact continuation quality is weak on realistic local code/text: 0.561 accepted tokens/query and 7.8% accepted/drafted with 8-token drafts. A min-4-token context gate improved precision to 18.2% accepted/drafted but reduced accepted tokens/query to 0.376. The mechanism only showed a modest positive-control signal on highly repetitive templates at 1.319 accepted tokens/query.

## Boundaries and scale limits

No real tokenizer, no language-model verifier, no KV-cache integration, no end-to-end local inference speed measurement, and corpora are small local/proxy datasets. Evidence supports only draft-source quality at this bounded scale.

## Claim scope

Bounded proxy evaluation of suffix-array draft generation over 90k-token train / 30k-token held-out splits for local code/text, synthetic repeated templates, and low-reuse generated text. The test measures oracle exact-token acceptance of drafted continuations, not end-to-end model latency.

## Why it stopped

Bounded proxy evidence shows low exact-token acceptance on realistic local code/text, so the mechanism is not paper-ready and does not justify a general local inference speedup claim without direct model-in-the-loop evidence.

## Recommended next action

Stop this run as a proxy early falsification of the broad suffix-array local-inference drafting claim; only pursue a bounded deepen follow-up if it adds real tokenizer/model verification and a gating policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop gated suffix-array drafting for local code completion
- Success threshold: At least 10% end-to-end tokens/s improvement over no drafting and fixed n-gram baselines on non-synthetic local-code prompts, with mean accepted tokens/query above 1.0 and no quality regression.
- Stop condition: Stop if gated suffix-array drafting stays below 1.0 accepted tokens/query or fails to improve end-to-end tokens/s by 10% on ordinary local-code prompts.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-draft-for-local-inference-5537e1aa0e0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
