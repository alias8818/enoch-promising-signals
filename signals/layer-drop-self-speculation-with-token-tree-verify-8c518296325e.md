# Layer-Drop Self-Speculation with Token-Tree Verify

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `layer-drop-self-speculation-with-token-tree-verify-8c518296325e`
Run ID: `layer-drop-self-speculation-with-token-tree-verify-8c518296325e-20260610T163252669114+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b835979da057

## What looked useful

Naive layer-drop self-speculation is an early negative: branch-2 depth-4 accepted only 0.125-0.25 tokens on average out of 4 and ran at 0.214-0.299x baseline speed; branch-4 depth-3 improved 9-layer acceptance to 0.8125 tokens on average but slowed to 0.080x baseline.

## Boundaries and scale limits

Tested only GPT-2 small, greedy verification, WikiText-2 validation prompts, PyTorch eager inference, no production KV-cache tree kernel, no trained early-exit heads, no larger models.

## Claim scope

For GPT-2 small using untrained layer-dropped drafts formed from the first 3, 6, or 9 of 12 blocks, small branch-2 and branch-4 token trees do not accept enough full-model greedy tokens to offset draft construction plus batched verification overhead.

## Why it stopped

Proxy/early falsification: the directly tested untrained GPT-2 layer-drop draft plus token-tree verifier had low acceptance and slower measured inference, so the naive mechanism is not viable in this bounded setup.

## Recommended next action

Stop this no-paper run; only revisit with trained early-exit/layer-drop heads or a fused KV-cache tree verifier, using the present GPT-2 acceptance metrics as the baseline to beat.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train Early-Exit Heads for Layer-Drop Token-Tree Self-Speculation
- Success threshold: Mean accepted tokens >=2.0 out of 4 for branch-2 depth-4 with measured tree total time at least 1.2x faster than greedy GPT-2 baseline on held-out prompts.
- Stop condition: Stop if trained heads fail to reach mean accepted tokens >=1.0 out of 4 or remain slower than 0.8x baseline after one bounded training run.

## Evidence references

- Artifact root: `<local-path>/projects/layer-drop-self-speculation-with-token-tree-verify-8c518296325e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
