# BitNet-b1.58 + Sparse FP8 Residual Channels on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bitnet-b1-58-sparse-fp8-residual-channels-on-gpt-2-small-59241c15ec92`
Run ID: `bitnet-b1-58-sparse-fp8-residual-channels-on-gpt-2-small-59241c15ec92-20260629T155942174582+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10d46b4777d6

## What looked useful

Sparse FP8 residual channels recover some damage from ternary-only quantization but remain far from dense GPT-2-small quality: all-block 20% residual channels gave PPL 7770.92 versus dense 35.59, 75% residual channels still gave PPL 717.31, while 100% FP8 residual channels gave PPL 35.66.

## Boundaries and scale limits

Evaluated pretrained GPT-2-small on 16,384 WikiText-2 validation tokens per run; no training, fine-tuning, full validation pass, learned channel selection, or native sparse-FP8 serving kernel was tested.

## Claim scope

Post-training GPT-2-small weight reconstruction on a bounded WikiText-2 validation subset: BitNet-style ternary weights plus sparse FP8 output-channel residuals do not preserve useful perplexity at sparse residual budgets; full FP8 residual reconstruction is a sanity check that nearly recovers dense quality.

## Why it stopped

Proxy/bounded early falsification rather than full validation: direct post-training GPT-2-small subset evidence shows sparse FP8 residual channels are not enough to make ternary GPT-2-small usable, although training-time variants could still overturn it.

## Recommended next action

Stop this post-training variant as no-paper evidence; if continuing, run a bounded quantization-aware fine-tuning follow-up with learned residual-channel selection and require near-dense validation perplexity at <=20% residual channels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware fine-tuning for BitNet GPT-2-small with learned FP8 residual channels
- Success threshold: At <=20% FP8 residual channels, achieve validation perplexity within 1.5x of the dense or dense-fine-tuned baseline on the bounded subset and outperform ternary-only by at least 5x PPL ratio.
- Stop condition: Stop if after a calibrated short QAT run the <=20% residual variant remains >3x dense perplexity or fails to beat random residual-channel selection.

## Evidence references

- Artifact root: `<local-path>/projects/bitnet-b1-58-sparse-fp8-residual-channels-on-gpt-2-small-59241c15ec92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
