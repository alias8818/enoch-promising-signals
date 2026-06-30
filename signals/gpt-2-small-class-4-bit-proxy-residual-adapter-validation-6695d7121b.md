# GPT-2-small-class 4-bit proxy residual adapter validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b`
Run ID: `gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b-20260605T035001305558+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 4-bit Proxy Residual Training: enoch://control-plane/projects/4-bit-proxy-residual-training-67024687d419/runs/4-bit-proxy-residual-training-67024687d419-20260604T223601041484+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5938b088e934

## What looked useful

Residual bottleneck adapters with 294,912 trainable parameters reduced fake-int4 GPT-2 small validation loss from 13.2065 to 4.8888 and 4.9386 across two seeds, close to fp32 pretrained loss 4.3183 but not matching it.

## Boundaries and scale limits

Small Tier 1 direct test only: fake quantization rather than packed int4 kernels, embeddings left fp32, 512 train sequences, 128 validation sequences, 80 steps, Wikitext-2 only, no LoRA/bias-only/parameter-matched baseline suite, no throughput or memory-serving validation.

## Claim scope

In a GPT-2 small pretrained model with deterministic fake-int4 quantization of Conv1D/Linear weights and fp32 embeddings, rank-16 residual block adapters trained for 80 steps on a small Wikitext-2 slice recovered about 93% of the validation loss gap created by the quantization proxy across two seeds.

## Why it stopped

Strict paper gate: this run produced useful bounded mechanism evidence, but proxy quantization and limited controls make it no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a deeper controlled validation with real int4 quantization and parameter-matched LoRA, bias-only, and residual-adapter controls on a larger held-out text slice before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-int4 GPT-2 small residual adapter versus matched adapter baselines
- Success threshold: Residual adapters recover at least 80% of the fp32-vs-int4 validation loss gap, beat bias-only by at least 10% relative gap recovery, and are within 5% relative gap recovery of or better than matched LoRA across at least three seeds.
- Stop condition: Stop if real int4 residual adapters recover less than 50% of the loss gap or fail to outperform bias-only on two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
