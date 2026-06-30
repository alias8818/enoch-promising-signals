# Ternary-1.58b with 5% FP16 Residual Channels for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-1-58b-with-5-fp16-residual-channels-for-gpt-2-small-241f74ea3e95`
Run ID: `ternary-1-58b-with-5-fp16-residual-channels-for-gpt-2-small-241f74ea3e95-20260608T065310119847+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e2b1eb0a4bf6

## What looked useful

Top-error 5% FP16 residual channels reduced weighted relative weight MSE from 0.2862 to 0.2442 and improved perplexity from 674,479.53 to 23,349.05, but dense FP16 perplexity was 36.87 and random 5% residual channels were worse than full ternary. Channel choice matters, but the simple post-training 5% residual architecture is not viable.

## Boundaries and scale limits

Tested pretrained GPT-2-small only, projected Conv1D/Linear weights only, no embeddings/lm_head quantization, no training from scratch, no quantization-aware finetuning, no bit-packed inference kernel, and no full benchmark suite.

## Claim scope

Post-training GPT-2-small projected-weight conversion: 5% FP16 residual output channels selected by per-channel ternary reconstruction error improve over full ternary and random residual channels, but do not preserve language-model quality on an 8192-token WikiText-2 validation slice.

## Why it stopped

Proxy/early falsification of the post-training version: 5% top-error residual channels improved full ternary but remained about 633x worse than dense GPT-2-small perplexity on the direct target-model slice.

## Recommended next action

Run a bounded activation-aware residual-channel selection plus short quantization-aware finetuning probe on GPT-2-small; stop if the 5% residual variant cannot get within 2x dense-slice perplexity on the same WikiText-2 evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware 5% FP16 residual channels with short GPT-2-small QAT
- Success threshold: After bounded QAT, 5% residual ternary GPT-2-small reaches WikiText-2 slice perplexity no more than 2x the dense FP16 baseline while retaining approximately 5% FP16 residual projected weights.
- Stop condition: Stop as negative if activation-aware selection plus bounded QAT remains above 2x dense-slice perplexity or shows no sustained improvement over the weight-error residual baseline.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-1-58b-with-5-fp16-residual-channels-for-gpt-2-small-241f74ea3e95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
