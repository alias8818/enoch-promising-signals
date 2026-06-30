# INT8 Weight-Only Quantization Parity Test on GPT-2-124M Wikitext

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-weight-only-quantization-parity-test-on-gpt-2-124m-wikitext-30a3e340fd2c`
Run ID: `int8-weight-only-quantization-parity-test-on-gpt-2-124m-wikitext-30a3e340fd2c-20260619T130851837713+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfd9f4a57e07

## What looked useful

Primary run: FP32 perplexity 63.857757, INT8 weight-only perplexity 63.829634, relative delta -0.0440%, top-1 next-token agreement 97.77%, tensor bytes reduced from 497,759,232 to 243,287,040.

## Boundaries and scale limits

Not a full WikiText-2 run, not multiple seeds/windows, not an optimized INT8 kernel benchmark, not activation quantization, and not evidence for larger models or production serving.

## Claim scope

On this CPU worker, GPT-2-small (`gpt2`, 124M class) with all 48 transformer Conv1D projection modules replaced by symmetric per-output-channel INT8 weight-only tensors preserved perplexity on 16,384 contiguous WikiText-2 raw test tokens while reducing stored tensor bytes by 51.12%. Embeddings, layer norms, and lm_head remained FP32.

## Why it stopped

The bounded direct parity test supports the mechanism locally, but the evidence is too small and the implementation too proxy-like for optimized inference or paper-positive claims.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a full WikiText-2 test split plus a library-backed quantization baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full WikiText-2 GPT-2 INT8 weight-only parity with library baseline
- Success threshold: Relative perplexity regression under 1.0%, tensor-byte reduction at least 45%, and no repeated window with more than 5% relative local NLL degradation unexplained by tokenization/window artifacts.
- Stop condition: Stop as negative or mixed if full-split relative perplexity regression is at least 1.0%, if multiple windows show more than 5% local NLL degradation, or if a maintained baseline cannot reproduce the custom harness within the same qualitative parity band.

## Evidence references

- Artifact root: `<local-path>/projects/int8-weight-only-quantization-parity-test-on-gpt-2-124m-wikitext-30a3e340fd2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
