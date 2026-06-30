# Hot-window residual KV cache 2-bit compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hot-window-residual-kv-cache-2-bit-compression-dc62d54d817b`
Run ID: `hot-window-residual-kv-cache-2-bit-compression-dc62d54d817b-20260608T103913436102+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f51065dc37c2

## What looked useful

Hot-window 2-bit compression produced small MSE reductions versus all-cache 2-bit: 15.20% at seq512/W128 and 6.77% at seq1024/W128 for the residual variant. Residual centering was effectively indistinguishable from ordinary 2-bit quantization. Hot-window 4-bit reduced MSE by about 95.6-96.6% at similar but higher memory ratios, making the tested 2-bit residual scheme unattractive.

## Boundaries and scale limits

No end-to-end perplexity, task accuracy, packed-kernel latency, large-model serving, or long-context production decode was measured. Results are limited to local GPT-2 attention tensors up to seq1024 and synthetic tensors.

## Claim scope

Bounded GPT-2 attention-tensor proxy and synthetic stress tests show that exact recent-token hot windows modestly reduce 2-bit KV attention-output error, but the tested residual-centered 2-bit method adds no measurable benefit and remains far worse than a hot-window 4-bit control.

## Why it stopped

Proxy early falsification: the tested hot-window residual 2-bit scheme did not deliver a strong enough numerical benefit and was dominated by a 4-bit control; this is not full validation of all possible 2-bit KV designs.

## Recommended next action

Stop this variant as a no-paper early negative; if continuing locally, test a materially different outlier-aware or nonuniform 2-bit KV quantizer against the same GPT-2 attention-output proxy before any larger serving experiment.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Outlier-aware hot-window 2-bit KV quantization
- Success threshold: At seq1024, W<=128, achieve >=40% output-MSE reduction versus all-cache 2-bit at <=0.25 fp16 KV memory ratio and improve mean cosine by >=0.03, with residual metadata included in the memory accounting.
- Stop condition: Stop if the new 2-bit method improves output MSE by <20% versus all-cache 2-bit or requires >0.30 fp16 KV memory ratio before packed-kernel overhead.

## Evidence references

- Artifact root: `<local-path>/projects/hot-window-residual-kv-cache-2-bit-compression-dc62d54d817b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
