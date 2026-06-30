# End-to-End GPT-2 Perplexity Test for INT1 Variance Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-gpt-2-perplexity-test-for-int1-variance-residua-058acb122b`
Run ID: `end-to-end-gpt-2-perplexity-test-for-int1-variance-residua-058acb122b-20260523T193942933446+0000`

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

- Parent run decision: Activation-Variance Residual Channels at INT1: enoch://control-plane/projects/activation-variance-residual-channels-at-int1-a7612ad4ace3/runs/activation-variance-residual-channels-at-int1-a7612ad4ace3-20260523T184743756538+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e93004b3c107

## What looked useful

Variance-selected residual channels recovered some GPT-2 perplexity versus pure INT1 and beat sampled 10% random residual controls, but best PPL was still 28,470 versus 23.7 full precision and the residual-fraction curve was nonmonotonic, so static variance residual channels are not a viable end-to-end GPT-2 INT1 perplexity method by themselves.

## Boundaries and scale limits

Small direct post-training quantization test only: 65,472 evaluated next-token positions, GPT-2-small only, embeddings/layer norms/biases/LM head held full precision, no training-aware quantization, no full benchmark sweep.

## Claim scope

Pretrained GPT-2-small transformer projection matrices evaluated on 64 WikiText-2 validation blocks with per-output-channel scaled INT1 binary weights and static weight-variance-selected full-precision residual output channels.

## Why it stopped

Direct Tier 1 GPT-2 perplexity evidence was mixed: mechanism support exists versus pure INT1 and random controls, but all tested variance residual settings remain orders of magnitude from baseline perplexity and are not paper-positive.

## Recommended next action

Stop this static-variance INT1 residual claim as no-paper; the bounded next useful test is activation-error-selected residual channels on the same GPT-2/WikiText-2 harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Error Residual Channel Selection for INT1 GPT-2 Projections
- Success threshold: At 10% residual-channel budget, activation-error selection recovers at least 50% of the pure-INT1-to-full-precision mean-NLL gap and beats static variance and all random controls on held-out validation perplexity.
- Stop condition: Stop if activation-error selection recovers less than 35% of the NLL gap or fails to beat static variance at the same 10% residual budget on the held-out validation slice.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-perplexity-test-for-int1-variance-residua-058acb122b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
