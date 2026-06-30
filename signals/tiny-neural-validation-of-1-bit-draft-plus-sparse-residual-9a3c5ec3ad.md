# Tiny neural validation of 1-bit draft plus sparse residual correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-neural-validation-of-1-bit-draft-plus-sparse-residual-9a3c5ec3ad`
Run ID: `tiny-neural-validation-of-1-bit-draft-plus-sparse-residual-9a3c5ec3ad-20260527T063643229231+0000`

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

- Parent run decision: 1-bit draft with residual correction: enoch://control-plane/projects/1-bit-draft-with-residual-correction-731872c83f5e/runs/1-bit-draft-with-residual-correction-731872c83f5e-20260525T025731025429+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d6ad506a8a39

## What looked useful

Naive post-training top-k residual correction has a real mechanism signal but misses the 10% density threshold. In the five-seed confirmation sweep, dense accuracy was 0.9357, 1-bit draft accuracy was 0.8752, 10% top-k residual accuracy was 0.9101, random residual accuracy was 0.8821, gap recovery was 0.5802, and top-k beat random by 0.0280. At 30% density, gap recovery reached 0.8717.

## Boundaries and scale limits

Only a 784-128-10 MLP on MNIST subsets was tested. No transformer, language-model perplexity, generation quality, training-time representation, large-model scaling, hardware throughput, or memory-bandwidth result was measured.

## Claim scope

Small direct post-training neural test on a NumPy MNIST MLP: 1-bit sign-and-scale draft weights plus top-absolute sparse residual entries consistently improve accuracy over the 1-bit draft and over matched random residual controls, but 10% residual density does not recover 80% of the dense-vs-1-bit accuracy gap.

## Why it stopped

The controlled small direct test falsified the pre-registered 10% residual recovery threshold for naive post-training top-k residuals, while leaving a useful mechanism signal at higher residual densities.

## Recommended next action

Run a bounded transformer or GPT-2-small-class language-model follow-up with dense, 1-bit draft, top-k residual, random residual, and optionally learned-mask controls; stop if 10% residual density again recovers less than 80% of the 1-bit degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded language-model validation of 1-bit draft plus sparse residual correction
- Success threshold: At 10% residual density, recover at least 80% of the dense-vs-1-bit validation-loss or perplexity degradation and beat matched random residual controls by a practically meaningful margin across at least three seeds.
- Stop condition: Stop as no-paper negative if 10% residual density recovers less than 80% of the 1-bit degradation or fails to beat random residual controls on the bounded language-model task.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-neural-validation-of-1-bit-draft-plus-sparse-residual-9a3c5ec3ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
