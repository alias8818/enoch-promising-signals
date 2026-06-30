# KV-Cache Int2 with Residual Error Accumulation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-int2-with-residual-error-accumulation-48b5b7955040`
Run ID: `kv-cache-int2-with-residual-error-accumulation-48b5b7955040-20260602T145041629927+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ffbf8f38a301

## What looked useful

Residual feedback reduced medium-run K/V cumulative-sum MSE to about 0.22% of naive int2, but increased causal attention output MSE by 45.9%, increased attention L1 by 14.7%, reduced top-1 attention match by 6.7 percentage points, and more than doubled per-token K/V cache MSE.

## Boundaries and scale limits

Synthetic traces only; no pretrained-model KV activations, perplexity, generation-quality, packed-kernel throughput, or long-context serving measurements were run.

## Claim scope

On synthetic autoregressive causal-attention KV traces, simple temporal residual/error-feedback accumulation for per-token 2-bit KV-cache quantization dramatically reduces cumulative-sum error but worsens the full KV attention-output error versus ordinary per-token int2 quantization.

## Why it stopped

Proxy CUDA evidence directly tested causal attention fidelity and found the simple residual int2 KV method worse than naive int2 KV on the medium run; this is not a full real-model validation.

## Recommended next action

Stop this simple residual-accumulation variant as an early proxy falsification; only revisit with a real-KV replay or a salience-aware residual variant that avoids injecting residual error into individually attended value vectors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay residual int2 KV quantization on real GPT-2-small KV traces
- Success threshold: Residual int2 KV must reduce real-trace attention output MSE by at least 10% versus naive int2 KV without lowering top-1 attention agreement or worsening replay perplexity/logit error.
- Stop condition: Stop if real-trace residual int2 KV again increases attention output MSE or reduces top-1 attention agreement versus naive int2 KV.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int2-with-residual-error-accumulation-48b5b7955040`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
