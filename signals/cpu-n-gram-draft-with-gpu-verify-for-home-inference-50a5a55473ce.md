# CPU N-Gram Draft with GPU Verify for Home Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-n-gram-draft-with-gpu-verify-for-home-inference-50a5a55473ce`
Run ID: `cpu-n-gram-draft-with-gpu-verify-for-home-inference-50a5a55473ce-20260527T210143501535+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c64e4140781c

## What looked useful

CPU n-gram lookup was cheap, but exact acceptance was only about 0.16 tokens per verifier call. Verifier call reduction topped out at 1.164x under zero overhead and fell below break-even for draft lengths 4 and 8 at alpha=0.05; draft length 2 only reached 1.032x at alpha=0.05 and fell below break-even at alpha=0.10.

## Boundaries and scale limits

Proxy text replay only; no real LLM logits, no BPE tokenizer, no KV-cache timing, no implemented GPU verifier loop, one public-domain corpus, and one Python dictionary n-gram implementation.

## Claim scope

Plain corpus-trained CPU n-gram drafting, evaluated by exact held-out continuation replay on 30,000 regex tokens from tiny Shakespeare, does not provide robust modeled speedup unless GPU verifier overhead is extremely low.

## Why it stopped

Proxy early falsification: low exact acceptance leaves only a narrow speedup margin and does not support a paper or broad home-inference acceleration claim.

## Recommended next action

Stop this plain n-gram variant; a bounded follow-up should test prompt-local or domain-local n-gram drafting inside a real small-model verifier loop before any larger scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-local n-gram drafter with real small-model GPU verifier
- Success threshold: Median end-to-end speedup at least 1.10x with no text divergence, and lower confidence bound above 1.0x on the targeted repetitive/code-like prompt subset.
- Stop condition: Stop if exact acceptance remains below 0.5 tokens per verifier call or measured verifier overhead erases speedup on the first 30 prompts.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-with-gpu-verify-for-home-inference-50a5a55473ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
