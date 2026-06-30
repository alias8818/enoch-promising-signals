# Internal FFN-Slice Self-Draft Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `internal-ffn-slice-self-draft-speculation-6c0f422f044f`
Run ID: `internal-ffn-slice-self-draft-speculation-6c0f422f044f-20260530T042151116928+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c14bdb765dcf

## What looked useful

Across three seeds, the full proxy model reached about 0.397 validation target top-1 accuracy. Greedy agreement between slice logits and full logits rose with slice size: best mean agreement was about 0.236 at 3.125% channels, 0.336 at 6.25%, 0.416 at 12.5%, 0.545 at 25%, and 0.723 at 50%. High full-margin positions were much more slice-agreeable, with 25% prefix slices agreeing about 0.827 on top-quartile margin cases but only about 0.323 on low-margin cases.

## Boundaries and scale limits

This run did not test pretrained Transformer MLP internals, GPT-2-small-class baselines, real speculative decoding kernels, multi-token draft acceptance, sampling acceptance, KV-cache interactions, or wall-clock tokens/sec. The model is a small character MLP proxy with 512 hidden FFN channels and three seeds.

## Claim scope

In a self-contained NumPy character-level MLP language-model proxy trained on Tiny Shakespeare, partial FFN hidden-channel slices contain measurable next-token signal and can match the full model's greedy next-token choice above chance; however, unconditional cheap slices are weak and useful agreement appears only at relatively large slice fractions or high-margin positions.

## Why it stopped

Closed as a proxy useful-signal result rather than a full validation: the experiment directly tested FFN slice agreement in a small MLP language model, but not actual Transformer FFN slices or real speculative decoding speed.

## Recommended next action

Run a bounded direct pretrained Transformer hook probe on GPT-2-small-class or Pythia-70M-class MLP activations with confidence-gated slice drafting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Transformer FFN-slice draft agreement with confidence gating
- Success threshold: At <=25% MLP slice compute, achieve at least 60% greedy full-model agreement on ungated positions or a confidence-gated operating point with >=50% coverage and >=75% agreement; any speed claim must show measured tokens/sec improvement with quality parity.
- Stop condition: Stop if <=25% slices remain below 60% greedy agreement and no confidence-gated point reaches both 50% coverage and 75% agreement, because the proxy signal would not transfer strongly enough to justify decoder implementation.

## Evidence references

- Artifact root: `<local-path>/projects/internal-ffn-slice-self-draft-speculation-6c0f422f044f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
