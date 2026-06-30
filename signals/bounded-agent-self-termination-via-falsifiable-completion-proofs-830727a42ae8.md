# Bounded Agent Self-Termination via Falsifiable Completion Proofs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-agent-self-termination-via-falsifiable-completion-proofs-830727a42ae8`
Run ID: `bounded-agent-self-termination-via-falsifiable-completion-proofs-830727a42ae8-20260531T105721431182+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/059565658986

## What looked useful

Completion proofs work as a specification/verifier discipline for encoded predicates, but they do not solve semantic task completion unless the verifier obligations cover the actual requirements. Weak or incomplete verifiers reintroduce false termination.

## Boundaries and scale limits

Evidence is synthetic and idealized. It does not test real LLM agents, natural-language task ambiguity, adversarial proof fabrication, tool trace extraction, or human semantic acceptance. Hidden requirements deliberately outside the verifier remain uncertified.

## Claim scope

In a deterministic synthetic bounded-task simulator, a self-termination gate requiring exact machine-checkable evidence for every declared predicate eliminated premature termination on declared predicates across 60,000 main-run proof-gate episodes and two ablations.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the encoded-predicate mechanism but falsifies any broad claim that completion proofs alone guarantee semantic completion.

## Recommended next action

Run a bounded real-agent trace benchmark where agents emit completion proofs, independent checks score declared predicates, and humans label premature termination on semantic task requirements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Completion Proof Trace Benchmark
- Success threshold: At least a 50% relative reduction in human-labeled premature termination versus naive self-termination, with no more than 20% relative increase in budget exhaustion, and a demonstrated monotonic relation between predicate coverage and reduced false stops.
- Stop condition: Stop if proof generation fails on more than 30% of tasks, if declared-predicate false stops are not reduced by at least 30%, or if human-labeled false stops remain unchanged despite complete declared-predicate checks.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-agent-self-termination-via-falsifiable-completion-proofs-830727a42ae8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
